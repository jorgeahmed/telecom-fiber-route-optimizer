import networkx as nx
import matplotlib.pyplot as plt

def create_network():
    """
    Creates a weighted graph representing potential fiber routes between cities.
    Weights represent distance/cost in km.
    """
    # Nodes: City Hubs
    # Edges: (City A, City B, Cost)
    routes = [
        ('Hub_A', 'Hub_B', 10),
        ('Hub_A', 'Hub_C', 15),
        ('Hub_B', 'Hub_D', 12),
        ('Hub_C', 'Hub_D', 10),
        ('Hub_B', 'Hub_E', 20),
        ('Hub_D', 'Hub_E', 5)
    ]
    
    G = nx.Graph()
    for u, v, weight in routes:
        G.add_edge(u, v, weight=weight)
    
    return G

def optimize_route(G):
    """
    Calculates the Minimum Spanning Tree (MST) to connect all hubs 
    with the minimum total cable length.
    """
    print("[LOGIC] Calculating Minimum Spanning Tree (MST)...")
    mst = nx.minimum_spanning_tree(G)
    
    total_cost = sum(d['weight'] for u, v, d in mst.edges(data=True))
    print(f"[RESULT] Optimized Total Distance: {total_cost}km")
    print(f"[RESULT] Active Connections: {list(mst.edges())}")
    
    return mst

def visualize(G, mst):
    pos = nx.spring_layout(G)
    
    plt.figure(figsize=(8, 6))
    
    # Draw all potential routes (grey)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='lightgray', style='dashed')
    
    # Draw optimized routes (green)
    nx.draw(mst, pos, with_labels=True, node_color='lightgreen', edge_color='green', width=2)
    
    plt.title("Fiber Route Optimization (MST)")
    plt.show() # In a real app, this would save to a file
    print("[INFO] Visualization generated.")

if __name__ == "__main__":
    print("--- Telecom Fiber Route Optimizer ---")
    network = create_network()
    optimized_network = optimize_route(network)
    # visualize(network, optimized_network) # Uncomment to run with GUI
