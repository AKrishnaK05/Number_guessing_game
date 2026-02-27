import networkx as nx
import matplotlib.pyplot as plt

def build_graph(root):
    G = nx.DiGraph()
    pos = {}
    labels = {}

    def dfs(node, x=0, y=0, layer=1):
        if not node:
            return
        pos[node.value] = (x, y)
        labels[node.value] = str(node.value)

        if node.left:
            G.add_edge(node.value, node.left.value)
            dfs(node.left, x - 1 / (2**layer), y - 1, layer + 1)

        if node.right:
            G.add_edge(node.value, node.right.value)
            dfs(node.right, x + 1 / (2**layer), y - 1, layer + 1)

    dfs(root)
    return G, pos, labels

def render_tree_state(root, path, current_val=None, is_inconsistent=False):
    """Renders the current state of the tree for Streamlit."""
    G, pos, labels = build_graph(root)
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Node colors
    node_colors = []
    for node in G.nodes():
        if node == current_val:
            node_colors.append("#FF4B4B") # Current guess
        elif node in path:
            node_colors.append("#2EB100") # Visited path
        else:
            node_colors.append("#ADD8E6") # Potential targets
            
    if is_inconsistent and current_val in G.nodes():
        node_colors[list(G.nodes()).index(current_val)] = "#808080" # Gray out if failed

    # Draw edges
    edge_colors = []
    for u, v in G.edges():
        if u in path and v in path and path.index(v) == path.index(u) + 1:
            edge_colors.append("#2EB100") # Red path
        else:
            edge_colors.append("#CCCCCC")

    nx.draw(G, pos, labels=labels, with_labels=True, 
            node_color=node_colors, edge_color=edge_colors,
            node_size=800, font_size=8, font_weight='bold', 
            arrows=True, arrowsize=15, ax=ax)
    
    ax.set_title("Binary Decision Tree - Real-time Traversal", fontsize=15, fontweight='bold', color="#31333F")
    plt.axis('off')
    return fig
