import osmnx as ox
import matplotlib.pyplot as plt
import networkx as nx

place_name = "Belo Horizonte, Minas Gerais, Brasil"

filter = '["highway"~"primary|secondary|tertiary"]'

G = ox.graph_from_place(place_name, network_type="walk", custom_filter=filter)
G = ox.project_graph(G)

def shortest_path(source, target):
    source_point = ox.geocode(source + ", " + place_name)
    target_point = ox.geocode(target + ", " + place_name)
    
    source_node = ox.distance.nearest_nodes(G, source_point[1], source_point[0])
    target_node = ox.distance.nearest_nodes(G, target_point[1], target_point[0])
    
    route = nx.shortest_path(G, source_node, target_node, weight="length")
    
    return route

def format_route(route):
    if isinstance(route, str):
        return route
    
    coords = [(G.nodes[n]['y'], G.nodes[n]['x']) for n in route]
    return f"Path with {len(coords)} points: {coords[3:]} ... {coords[-3:]}"