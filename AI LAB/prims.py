'''
    Prim’s Algorithm is a greedy algorithm that finds a minimum spanning tree (MST) for a weighted undirected graph. In simpler terms, it helps you connect all the dots (or nodes) in the most efficient way possible, minimizing the total weight (or cost) of the connections.  
'''

import sys


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def printMST(self, parent):
        print("Edge \tWeight")
        total_weight = 0
        for i in range(1, self.V):
            if parent[i] is not None:
                weight = self.graph[i][parent[i]]
                print(parent[i], "-", i, "\t", weight)
                total_weight += weight
            else:
                print(f"Vertex {i} is not connected to MST")
        print(f"\nTotal MST Weight: {total_weight}")
        return total_weight
    
    def minKey(self, key, mstSet):
        min_val = sys.maxsize
        min_index = -1
        for v in range(self.V):
            if key[v] < min_val and mstSet[v] == False:
                min_val = key[v]
                min_index = v
        return min_index
    
    def primMST(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        mstSet = [False] * self.V
        key[0] = 0
        parent[0] = -1
        
        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            if u == -1:  # No more vertices to process
                break
            mstSet[u] = True
            
            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
        
        return parent


def test_prims_algorithm():
    """Test cases for Prim's MST algorithm"""
    print("=" * 50)
    print("Testing Prim's MST Algorithm")
    print("=" * 50)
    
    # Test Case 1: Simple 4-vertex graph
    print("\nTest Case 1: Simple 4-vertex graph")
    print("-" * 30)
    g1 = Graph(4)
    g1.graph = [
        [0, 10, 6, 5],
        [10, 0, 0, 15],
        [6, 0, 0, 4],
        [5, 15, 4, 0]
    ]
    
    print("Graph adjacency matrix:")
    for row in g1.graph:
        print(row)
    
    parent1 = g1.primMST()
    print("\nMST edges:")
    weight1 = g1.printMST(parent1)
    
    # Test Case 2: Complex 6-vertex graph
    print("\n\nTest Case 2: Complex 6-vertex graph")
    print("-" * 30)
    g2 = Graph(6)
    g2.graph = [
        [0, 4, 6, 0, 0, 0],
        [4, 0, 6, 3, 4, 0],
        [6, 6, 0, 1, 8, 0],
        [0, 3, 1, 0, 2, 3],
        [0, 4, 8, 2, 0, 7],
        [0, 0, 0, 3, 7, 0]
    ]
    
    print("Graph adjacency matrix:")
    for row in g2.graph:
        print(row)
    
    parent2 = g2.primMST()
    print("\nMST edges:")
    weight2 = g2.printMST(parent2)
    
    # Test Case 3: Single vertex (edge case)
    print("\n\nTest Case 3: Single vertex graph")
    print("-" * 30)
    g3 = Graph(1)
    g3.graph = [[0]]
    
    print("Graph adjacency matrix:")
    for row in g3.graph:
        print(row)
    
    parent3 = g3.primMST()
    print("\nMST edges:")
    weight3 = g3.printMST(parent3)
    
    # Test Case 4: Disconnected graph
    print("\n\nTest Case 4: Disconnected graph")
    print("-" * 30)
    g4 = Graph(4)
    g4.graph = [
        [0, 2, 0, 0],
        [2, 0, 0, 0],
        [0, 0, 0, 3],
        [0, 0, 3, 0]
    ]
    
    print("Graph adjacency matrix:")
    for row in g4.graph:
        print(row)
    
    parent4 = g4.primMST()
    print("\nMST edges:")
    weight4 = g4.printMST(parent4)
    
    # Test Case 5: Complete graph
    print("\n\nTest Case 5: Complete graph")
    print("-" * 30)
    g5 = Graph(5)
    g5.graph = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0]
    ]
    
    print("Graph adjacency matrix:")
    for row in g5.graph:
        print(row)
    
    parent5 = g5.primMST()
    print("\nMST edges:")
    weight5 = g5.printMST(parent5)
    
    # Summary of all test cases
    print("\n" + "=" * 50)
    print("SUMMARY OF MST WEIGHTS")
    print("=" * 50)
    print(f"Test Case 1 (4-vertex): {weight1}")
    print(f"Test Case 2 (6-vertex): {weight2}")
    print(f"Test Case 3 (1-vertex): {weight3}")
    print(f"Test Case 4 (disconnected): {weight4}")
    print(f"Test Case 5 (complete): {weight5}")


def calculate_mst_weight(graph, parent):
    """Calculate the total weight of the MST"""
    total_weight = 0
    for i in range(1, graph.V):
        if parent[i] is not None:
            total_weight += graph.graph[i][parent[i]]
    return total_weight


def main():
    """Main function to demonstrate Prim's algorithm"""
    print("Prim's Minimum Spanning Tree Algorithm")
    print("=====================================")
    
    # Run test cases
    test_prims_algorithm()
    
    print("\n" + "=" * 50)
    print("Interactive Example")
    print("=" * 50)
    
    # Interactive example
    vertices = int(input("Enter number of vertices: "))
    g = Graph(vertices)
    
    print(f"Enter the adjacency matrix ({vertices}x{vertices}):")
    for i in range(vertices):
        row = list(map(int, input().split()))
        g.graph[i] = row
    
    print("\nYour graph:")
    for row in g.graph:
        print(row)
    
    parent = g.primMST()
    print("\nMST edges:")
    total_weight = g.printMST(parent)
    
    print(f"\nFinal MST weight: {total_weight}")


if __name__ == "__main__":
    main()