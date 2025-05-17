import osmnx as ox
import matplotlib.pyplot as plt
import requests

place_name = "Belo Horizonte, Minas Gerais, Brasil"

filter = '["highway"~"primary|secondary|tertiary"]'

G = ox.graph_from_place(place_name,
                        network_type="walk",
                        custom_filter=filter)

ox.plot_graph(G)