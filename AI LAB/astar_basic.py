import heapq

def a_star(graph, heuristic, start, goal):
    pq = [(heuristic[start], start)]
    cost = {start: 0}
    parent = {start: None}

    while pq:
        _, node = heapq.heappop(pq)

        if node == goal:
            path = []
            while node:
                path.append(node)
                node = parent[node]
            return path[::-1]

        for nei, wt in graph[node]:
            new_cost = cost[node] + wt
            if nei not in cost or new_cost < cost[nei]:
                cost[nei] = new_cost
                priority = new_cost + heuristic[nei]
                heapq.heappush(pq, (priority, nei))
                parent[nei] = node
graph = {
    'A': [('B',1), ('C',3)],
    'B': [('D',1)],
    'C': [('D',1)],
    'D': []
}

heuristic = {'A':3, 'B':2, 'C':1, 'D':0}

print(a_star(graph, heuristic, 'A', 'D'))
