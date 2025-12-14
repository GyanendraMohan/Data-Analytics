"""
Depth-First Search (DFS) Implementation for Graph Traversal

DFS is a graph traversal algorithm that explores as far as possible along 
each branch before backtracking. It uses a stack (or recursion) to maintain the path.
"""


def dfs(graph, vertex, visited):
    """
    Recursive DFS traversal starting from a given vertex.
    
    Args:
        graph: Dictionary representing adjacency list
        vertex: Starting vertex
        visited: Set to track visited vertices
    """
    visited.add(vertex)
    print(vertex, end=" ")
    
    for neighbor in graph.get(vertex, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


def is_connected(graph):
    """
    Check if graph is connected using DFS.
    
    Args:
        graph: Dictionary representing adjacency list
    
    Returns:
        True if graph is connected, False otherwise
    """
    if not graph:
        return True
    
    visited = set()
    start_vertex = list(graph.keys())[0]
    dfs(graph, start_vertex, visited)
    
    return len(visited) == len(graph)


if __name__ == "__main__":
    # Using dictionary to represent a graph
    graph = {
        0: [1, 2, 3],
        1: [0, 2],
        2: [0, 1, 4],
        3: [0],
        4: [2]
    }
    
    # Traverse the graph using DFS starting from node 0
    print("DFS Traversal (starting from 0):", end=" ")
    visited = set()
    dfs(graph, 0, visited)
    print()
    print("Visited vertices:", sorted(visited))
    
    # Check if graph is connected
    print()
    if is_connected(graph):
        print("The graph is connected")
    else:
        print("The graph is not connected")
