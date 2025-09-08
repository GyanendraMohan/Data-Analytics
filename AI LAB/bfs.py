import collections


def bfs(graph, start):
    visited = set()  # Set to keep track of visited nodes.
    queue = collections.deque([start]) # this will create a queue and add the starting node to it
    while queue:
        vertex = queue.popleft()  # Dequeue a vertex from queue
        visited.add(vertex)
        for i in graph[vertex]:
            if i not in visited:
                queue.append(i)
    print("visited",visited)

def dfs(graph, vertex, visited):
    visited.add(vertex)
    for adj in graph[vertex]:
        if adj not in visited:
            dfs(graph, adj, visited)

def is_connected(graph):
    visited = set()
    vertex = list(graph.keys())
    print("vertex",vertex)
    dfs(graph, vertex[0], visited)
    
    return len(visited) == len(graph)   
    

if __name__ == "__main__":
    #using dictionary to represent a graph
    graph = {
        0:[1,2,3],
        1:[0,2],
        2:[0,1,4],
        3:[0],
        4:[2],
    }
    # traverse the graph using BFS level by level starting from node 0
    #Queue to keep track of nodes to visit
    
    bfs(graph, 0)
    
    if is_connected(graph):
        print("The graph is connected")
    else:
        print("The graph is not connected")