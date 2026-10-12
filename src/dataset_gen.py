import random

# ============================================================
# 1. Generate a random connected weighted graph
# ============================================================

def generate_graph(V, E, seed=42):
    random.seed(seed)

    # Maximum possible edges for an undirected simple graph
    max_edges = V * (V - 1) // 2

    if E < V - 1:
        raise ValueError("E must be at least V-1 for a connected graph.")

    if E > max_edges:
        raise ValueError("Too many edges for this graph.")

    edges = set()
    seen = set()

    # First create a spanning tree so the graph is connected
    for vertex in range(1, V):
        parent = random.randint(0, vertex - 1)
        weight = random.randint(1, 100)
        u, v = min(vertex, parent), max(vertex, parent)
        seen.add((u, v))
        edges.add((u, v, weight))

    # Add random edges until we reach E
    while len(edges) < E:
        u = random.randint(0, V - 1)
        v = random.randint(0, V - 1)

        if u == v:
            continue

        u, v = min(u, v), max(u, v)

        if (u, v) in seen:
            continue

        weight = random.randint(1, 100)

        seen.add((u, v))
        edges.add((u, v, weight))

    return list(edges)


# ============================================================
# 2. Convert edges into adjacency matrix
# ============================================================

def edges_to_matrix(V, edges):
    matrix = [
        [float('inf')] * V
        for _ in range(V)
    ]

    for i in range(V):
        matrix[i][i] = 0

    for u, v, weight in edges:
        matrix[u][v] = weight
        matrix[v][u] = weight

    return matrix


# ============================================================
# 3. Convert edges into adjacency list
# ============================================================

def edges_to_list(V, edges):
    adj = [[] for _ in range(V)]

    for u, v, weight in edges:
        adj[u].append((v, weight))
        adj[v].append((u, weight))

    return adj
