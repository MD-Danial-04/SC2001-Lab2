import heapq


def djikstra(adj, src):
    V = len(adj)
    distance = [float('inf')] * V

    distance[src] = 0
    pq = [(0, src)]

    while pq:
        curr_dist, u = heapq.heappop(pq)
        if distance[u] != curr_dist:
            continue

        for vertex, edge in adj[u]:
            new_distance = curr_dist + edge

            if  new_distance < distance[vertex]:
                distance[vertex] = new_distance
                heapq.heappush(pq, (new_distance, vertex))

    return distance

if __name__ == "__main__":
    adj = [
        [(1,4), (2,2)],
        [(0,4), (2,1), (3,5)],
        [(0,2), (1,1), (3,3)],
        [(1,5), (2,3)]
    ]

    result = djikstra(adj, 0)
    print(result)
