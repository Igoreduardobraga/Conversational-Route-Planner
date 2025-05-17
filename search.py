import osmnx as ox
import matplotlib.pyplot as plt
import networkx as nx

place_name = "Belo Horizonte, Minas Gerais, Brasil"

filter = '["highway"~"primary|secondary|tertiary"]'

G = ox.graph_from_place(place_name, network_type="walk", custom_filter=filter)

def shortest_path(source, target):
    source_point = ox.geocode(source + ", " + place_name)
    target_point = ox.geocode(target + ", " + place_name)
    
    print("Source point (lat, lon):", source_point)
    print("Target point (lat, lon):", target_point)
    
    source_node = ox.distance.nearest_nodes(G, source_point[1], source_point[0])
    target_node = ox.distance.nearest_nodes(G, target_point[1], target_point[0])
    
    route = nx.shortest_path(G, source_node, target_node, weight="length")
    
    return route

def plot_route(route):
    fig, ax = ox.plot_graph_route(G, route, route_linewidth=4, node_size=0)
    plt.show()
    

def route_street_names(G, route):
    street_names = []
    for u, v in zip(route[:-1], route[1:]):
        edge_data = G.get_edge_data(u, v, 0)

        if edge_data is None:
            continue

        name = edge_data.get('name', None)

        if isinstance(name, list):
            name = ", ".join(name)
        if name is None:
            name = "Unnamed Road"

        if not street_names or street_names[-1] != name:
            street_names.append(name)

    return street_names


def format_route(route):
    if isinstance(route, str):
        return route

    streets = route_street_names(G, route)
    n_streets = len(streets)

    if n_streets == 0:
        return "No street names found on the route."

    streets_str = " -> ".join(streets)

    return f"Route with {len(streets)} street segments: {streets_str}"
