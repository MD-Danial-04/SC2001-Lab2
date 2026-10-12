def djikstra(adj, src):
    # Init
    V = len(adj)
    pq = list(range(V))
    distance = [float('inf')] * V
    visited = [False] * V

    # src
    distance[src] = 0
    u = src

    while pq and u != -1:
        # updating distances - relaxation
        for i in range(V):
            # check if not visited and edge exists
            if not visited[i] and adj[u][i] != float('inf'):
                new_distance = distance[u] + adj[u][i]

                # Check if new path is smaller than prev
                distance[i] = min(distance[i], new_distance)

        visited[u] = True
        pq.remove(u)

        # finding next node
        min_dist = float('inf')
        u = -1

        for i in pq:
           if distance[i] < min_dist:
               min_dist = distance[i]
               u = i

    return distance

# Time complexity it V^2

if __name__ == "__main__":
    # Initializing
    adj = [
        [0, 4, 2, float('inf')],
        [4, 0, 1, 5],
        [2, 1, 0, 3],
        [float('inf'), 5, 3, 0]
    ]

    adj_unreachable = [
        [0, 4, 2, float('inf')],
        [4, 0, 1, float('inf')],
        [2, 1, 0, float('inf')],
        [float('inf'), float('inf'), float('inf'), 0]
    ]

    adj_uno = [
        [0]
    ]
    src = 0

    result = djikstra(adj, src)
    print(result)
    result = djikstra(adj_unreachable, src)
    print(result)
    result = djikstra(adj_uno, src)
    print(result)
