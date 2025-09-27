"""
BICONNECTED COMPONENTS AND ARTICULATION POINTS

A biconnected component is a maximal biconnected subgraph.

A graph is said to be biconnected if:
1. It is connected, i.e. it is possible to reach every vertex from every other vertex, by a simple path.
2. Even after removing any vertex the graph remains connected.

A graph is biconnected if it has no vertex such that its removal increases the number of connected components in the graph. 
A vertex whose removal increases the number of connected components is called an Articulation Point.

ALGORITHMS IMPLEMENTED:
1. Tarjan's Algorithm for finding Articulation Points
2. Algorithm for finding Biconnected Components
"""

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        """
        Initialize graph with given number of vertices
        
        Args:
            vertices: Number of vertices in the graph
        """
        self.vertices = vertices
        self.adj = defaultdict(list)
        self.time = 0
        
    def add_edge(self, u, v):
        """
        Add an undirected edge between vertices u and v
        
        Args:
            u, v: Vertices to connect
        """
        self.adj[u].append(v)
        self.adj[v].append(u)
        
    def find_articulation_points(self):
        """
        Find all articulation points in the graph using Tarjan's algorithm
        
        ARTICULATION POINT ALGORITHM (Tarjan's DFS):
        1. Perform DFS and maintain discovery time and low link values
        2. A vertex is an articulation point if:
           - It's root and has more than one child in DFS tree, OR
           - It's not root and has a child with low link >= discovery time
        
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        
        Returns:
            list: List of articulation points
        """
        # Initialize arrays for DFS
        disc = [-1] * self.vertices  # Discovery time
        low = [-1] * self.vertices   # Low link value
        parent = [-1] * self.vertices # Parent in DFS tree
        ap = [False] * self.vertices  # Articulation points
        self.time = 0
        
        def dfs(u):
            # Count children of current vertex
            children = 0
            
            # Initialize discovery time and low link
            disc[u] = self.time
            low[u] = self.time
            self.time += 1
            
            # Visit all neighbors
            for v in self.adj[u]:
                if disc[v] == -1:  # Not visited
                    children += 1
                    parent[v] = u
                    dfs(v)
                    
                    # Update low link of u
                    low[u] = min(low[u], low[v])
                    
                    # Check if u is articulation point
                    if parent[u] == -1 and children > 1:
                        ap[u] = True
                    if parent[u] != -1 and low[v] >= disc[u]:
                        ap[u] = True
                        
                elif v != parent[u]:  # Back edge
                    low[u] = min(low[u], disc[v])
        
        # Run DFS for all components
        for i in range(self.vertices):
            if disc[i] == -1:
                dfs(i)
        
        # Return articulation points
        return [i for i in range(self.vertices) if ap[i]]
    
    def find_biconnected_components(self):
        """
        Find all biconnected components in the graph
        
        BICONNECTED COMPONENTS ALGORITHM:
        1. Use DFS to find articulation points
        2. Biconnected components are maximal subgraphs without articulation points
        3. Use stack to track edges and form components
        
        Time Complexity: O(V + E)
        Space Complexity: O(V + E)
        
        Returns:
            list: List of biconnected components (each component is a set of edges)
        """
        disc = [-1] * self.vertices
        low = [-1] * self.vertices
        parent = [-1] * self.vertices
        self.time = 0
        components = []
        stack = []
        
        def dfs(u):
            disc[u] = self.time
            low[u] = self.time
            self.time += 1
            
            for v in self.adj[u]:
                if disc[v] == -1:  # Tree edge
                    parent[v] = u
                    stack.append((u, v))  # Add edge to stack
                    dfs(v)
                    
                    low[u] = min(low[u], low[v])
                    
                    # If u is articulation point, pop stack to get component
                    if (parent[u] == -1 and len([child for child in self.adj[u] if parent[child] == u]) > 1) or \
                       (parent[u] != -1 and low[v] >= disc[u]):
                        component = []
                        while True:
                            edge = stack.pop()
                            component.append(edge)
                            if edge == (u, v):
                                break
                        components.append(component)
                        
                elif v != parent[u] and disc[v] < disc[u]:  # Back edge
                    low[u] = min(low[u], disc[v])
                    stack.append((u, v))
        
        # Run DFS for all components
        for i in range(self.vertices):
            if disc[i] == -1:
                dfs(i)
                
                # Handle remaining edges in stack (connected component)
                if stack:
                    component = []
                    while stack:
                        component.append(stack.pop())
                    components.append(component)
        
        return components
    
    def print_graph(self):
        """Print the adjacency list representation of the graph"""
        print("Graph representation:")
        for vertex in range(self.vertices):
            print(f"Vertex {vertex}: {self.adj[vertex]}")
        print()

# Test the implementation
if __name__ == "__main__":
    print("=== BICONNECTED COMPONENTS AND ARTICULATION POINTS ===\n")
    
    # Test Case 1: Graph with articulation points
    print("Test Case 1: Graph with articulation points")
    g1 = Graph(7)
    g1.add_edge(0, 1)
    g1.add_edge(1, 2)
    g1.add_edge(2, 0)
    g1.add_edge(1, 3)
    g1.add_edge(1, 4)
    g1.add_edge(1, 6)
    g1.add_edge(3, 5)
    g1.add_edge(4, 5)
    
    g1.print_graph()
    
    articulation_points = g1.find_articulation_points()
    print(f"Articulation Points: {articulation_points}")
    
    biconnected_components = g1.find_biconnected_components()
    print(f"Number of Biconnected Components: {len(biconnected_components)}")
    for i, component in enumerate(biconnected_components):
        print(f"Component {i+1}: {component}")
    print()
    
    # Test Case 2: Biconnected graph (no articulation points)
    print("Test Case 2: Biconnected graph (no articulation points)")
    g2 = Graph(4)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(2, 3)
    g2.add_edge(3, 0)
    g2.add_edge(0, 2)
    
    g2.print_graph()
    
    articulation_points = g2.find_articulation_points()
    print(f"Articulation Points: {articulation_points}")
    
    biconnected_components = g2.find_biconnected_components()
    print(f"Number of Biconnected Components: {len(biconnected_components)}")
    for i, component in enumerate(biconnected_components):
        print(f"Component {i+1}: {component}")
    print()
    
    print("=== ALGORITHM SUMMARY ===")
    print("1. ARTICULATION POINTS: Vertices whose removal increases connected components")
    print("2. BICONNECTED COMPONENTS: Maximal subgraphs without articulation points")
    print("3. Both algorithms use DFS with discovery time and low link values")
    print("4. Time Complexity: O(V + E)")
    print("5. Space Complexity: O(V + E)")

