import networkx as nx
import heapq

def dijkstra_with_networkx(graph, start):
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0  

    min_heap = [(0, start)]  

    while min_heap:
        current_distance, u = heapq.heappop(min_heap)

        if current_distance > distances[u]:
            continue

        for v in graph.neighbors(u):
            weight = graph[u][v]['weight']
            distance = current_distance + weight

            if distance < distances[v]:
                distances[v] = distance
                heapq.heappush(min_heap, (distance, v))  

    return distances


G = nx.Graph()
G.add_weighted_edges_from([
    ('A', 'B', 1),
    ('A', 'C', 4),
    ('B', 'C', 2),
    ('B', 'D', 5),
    ('C', 'D', 1)
])

start_vertex = 'A'

shortest_paths = dijkstra_with_networkx(G, start_vertex)

print("Найкоротші шляхи від вершини", start_vertex)
for vertex, distance in shortest_paths.items():
    print(f"Відстань до {vertex}: {distance}")
