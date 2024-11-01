import uuid
import networkx as nx
import matplotlib.pyplot as plt
import colorsys

class Node:
    def __init__(self, key, color='lightblue'):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  
        self.id = str(uuid.uuid4())  

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def heap_to_binary_tree(heap):
    if not heap:
        return None
    
    nodes = [Node(value) for value in heap]

    for i in range(len(nodes)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(nodes):
            nodes[i].left = nodes[left_index]
        if right_index < len(nodes):
            nodes[i].right = nodes[right_index]

    return nodes[0]  


def generate_color(index, max_index):
    hue = 0.6  
    saturation = 0.5  
    lightness = 0.3 + 0.7 * (index / max_index)  
    rgb = colorsys.hls_to_rgb(hue, lightness, saturation)
    return '#{:02x}{:02x}{:02x}'.format(int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))


def dfs_with_visualization(root):
    if not root:
        return
    stack = [root]
    visited_nodes = []
    index = 0

    while stack:
        node = stack.pop()
        if node not in visited_nodes:
            node.color = generate_color(index, 15) 
            visited_nodes.append(node)
            index += 1
             
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    draw_tree(root) 
    

def bfs_with_visualization(root):
    if not root:
        return
    queue = [root]
    visited_nodes = []
    index = 0

    while queue:
        node = queue.pop(0)
        if node not in visited_nodes:
            node.color = generate_color(index, 15)  
            visited_nodes.append(node)
            index += 1
            
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    draw_tree(root)  

heap = [10, 5, 3, 2, 4, 1]

root = heap_to_binary_tree(heap)
draw_tree(root)

print("Обхід в глибину (DFS):")
dfs_with_visualization(root)

print("Обхід в ширину (BFS):")
bfs_with_visualization(root)