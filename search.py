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


def format_route(route):
    if isinstance(route, str):
        return route

    coords = [(G.nodes[n]['y'], G.nodes[n]['x']) for n in route]
    n_points = len(coords)

    if n_points <= 6:
        coords_str = ", ".join([f"({y:.5f}, {x:.5f})" for y, x in coords])
    else:
        first_points = ", ".join(
            [f"({y:.5f}, {x:.5f})" for y, x in coords[:3]])
        last_points = ", ".join(
            [f"({y:.5f}, {x:.5f})" for y, x in coords[-3:]])
        coords_str = f"{first_points} ... {last_points}"

    return f"Path with {n_points} points: {coords_str}"
