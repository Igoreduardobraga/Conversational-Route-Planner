import osmnx as ox
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

place_name = "Belo Horizonte, Minas Gerais, Brasil"

filter = '["highway"~"primary|secundary|tertiary"]'

G = ox.graph_from_place(place_name, network_type="walk", custom_filter=filter)

restaurants = ox.features_from_place(place_name, {"amenity": "restaurant"})
restaurant_points = restaurants.representative_point()
nearest_nodes = ox.distance.nearest_nodes(
    G, restaurant_points.x, restaurant_points.y)

useful_tags = ["amenity", "name", "cuisine"]

restaurant_name_to_node = {}
for node, feature in zip(nearest_nodes, restaurants[useful_tags].to_dict(orient="records")):
    feature = {k: v for k, v in feature.items() if pd.notna(v)}
    if "name" in feature:
        restaurant_name_to_node[feature["name"].lower()] = node
    if "restaurants" not in G.nodes[node]:
        G.nodes[node]["restaurants"] = []
    G.nodes[node]["restaurants"].append(feature)

def shortest_path(source, target):
    source_node = None
    if source.lower() in restaurant_name_to_node:
        source_node = restaurant_name_to_node[source.lower()]
    else:
        source_point = ox.geocode(source + ", " + place_name)
        source_node = ox.distance.nearest_nodes(
            G, source_point[1], source_point[0])

    # Mesma coisa para target
    target_node = None
    if target.lower() in restaurant_name_to_node:
        target_node = restaurant_name_to_node[target.lower()]
    else:
        target_point = ox.geocode(target + ", " + place_name)
        target_node = ox.distance.nearest_nodes(
            G, target_point[1], target_point[0])
    
    bfs_route = bfs_path(G, source_node, target_node)
    a_star_route = a_star_path(G, source_node, target_node)
    
    return bfs_route, a_star_route

def bfs_path(G, source, target):
    try:
        return nx.shortest_path(G, source, target)
    except nx.NetworkXNoPath:
        return None
    
def a_star_path(G, source, target):
    try:
        return nx.astar_path(G, source, target, weight='length')
    except nx.NetworkXNoPath:
        return None

def plot_routes(route1, route2):
    fig, ax = ox.plot_graph(G, show=False, close=False)

    # Plotar rota BFS em azul
    if route1:
        ox.plot_graph_route(G, route1, route_linewidth=4,
                            route_color='blue', ax=ax, show=False, close=False)
    # Plotar rota A* em vermelho
    if route2:
        ox.plot_graph_route(G, route2, route_linewidth=4,
                            route_color='red', ax=ax, show=True, close=True)


def format_route(route):
    if isinstance(route, str):
        return route

    coords = [(G.nodes[n]['y'], G.nodes[n]['x']) for n in route]
    coords_str = ", ".join([f"({y:.5f}, {x:.5f})" for y, x in coords])

    return f"Path with {len(coords)} points: {coords_str}"
