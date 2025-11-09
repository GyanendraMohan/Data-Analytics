"""Basic A* Algorithm with Graph and Manual Heuristics"""

import heapq
from typing import Dict, List, Tuple, Optional, Set


class GraphNode:
    def __init__(self, name: str, heuristic: float = 0):
        self.name = name
        self.heuristic = heuristic
        self.neighbors: Dict[str, float] = {}  # neighbor_name: cost
        self.g_cost = float('inf')
        self.f_cost = float('inf')
        self.parent: Optional[str] = None
    
    def add_neighbor(self, neighbor_name: str, cost: float):
        self.neighbors[neighbor_name] = cost
    
    def __lt__(self, other):
        return self.f_cost < other.f_cost


class BasicAStar:
    def __init__(self):
        self.graph: Dict[str, GraphNode] = {}
    
    def add_node(self, name: str, heuristic: float = 0):
        self.graph[name] = GraphNode(name, heuristic)
    
    def add_edge(self, from_node: str, to_node: str, cost: float):
        if from_node in self.graph and to_node in self.graph:
            self.graph[from_node].add_neighbor(to_node, cost)
    
    def find_path(self, start: str, goal: str) -> Optional[List[str]]:
        if start not in self.graph or goal not in self.graph:
            return None
        
        # Initialize start node
        start_node = self.graph[start]
        start_node.g_cost = 0
        start_node.f_cost = start_node.heuristic
        
        open_set = [(start_node.f_cost, start)]
        closed_set: Set[str] = set()
        
        while open_set:
            current_f, current_name = heapq.heappop(open_set)
            current_node = self.graph[current_name]
            
            if current_name in closed_set:
                continue
            
            closed_set.add(current_name)
            
            if current_name == goal:
                return self.reconstruct_path(start, goal)
            
            for neighbor_name, edge_cost in current_node.neighbors.items():
                if neighbor_name in closed_set:
                    continue
                
                neighbor_node = self.graph[neighbor_name]
                tentative_g = current_node.g_cost + edge_cost
                
                if tentative_g < neighbor_node.g_cost:
                    neighbor_node.parent = current_name
                    neighbor_node.g_cost = tentative_g
                    neighbor_node.f_cost = tentative_g + neighbor_node.heuristic
                    heapq.heappush(open_set, (neighbor_node.f_cost, neighbor_name))
        
        return None
    
    def reconstruct_path(self, start: str, goal: str) -> List[str]:
        path = []
        current = goal
        
        while current is not None:
            path.append(current)
            current = self.graph[current].parent
        
        return path[::-1]
    
    def print_graph(self):
        print("Graph Structure:")
        print("-" * 40)
        for node_name, node in self.graph.items():
            print(f"Node {node_name}: heuristic={node.heuristic}")
            for neighbor, cost in node.neighbors.items():
                print(f"  -> {neighbor} (cost: {cost})")
        print("-" * 40)


def create_sample_graph() -> BasicAStar:
    """Create a sample graph for demonstration"""
    astar = BasicAStar()
    
    # Add nodes with their heuristic values (estimated distance to goal)
    astar.add_node("A", heuristic=10)
    astar.add_node("B", heuristic=8)
    astar.add_node("C", heuristic=5)
    astar.add_node("D", heuristic=7)
    astar.add_node("E", heuristic=3)
    astar.add_node("F", heuristic=6)
    astar.add_node("G", heuristic=5)
    astar.add_node("H", heuristic=3)
    astar.add_node("I", heuristic=1)
    astar.add_node("J", heuristic=0)  # Goal node
    
    # Add edges (connections between nodes with costs)
    astar.add_edge("A", "B", 5)
    astar.add_edge("A", "C", 3)
    astar.add_edge("B", "D", 4)
    astar.add_edge("B", "E", 2)
    astar.add_edge("C", "D", 1)
    astar.add_edge("C", "F", 7)
    astar.add_edge("D", "G", 2)
    astar.add_edge("E", "H", 3)
    astar.add_edge("F", "G", 1)
    astar.add_edge("F", "H", 2)
    astar.add_edge("G", "I", 3)
    astar.add_edge("H", "I", 2)
    astar.add_edge("I", "J", 4)
    
    return astar


def main():
    print("Basic A* Algorithm with Graph")
    print("=" * 50)
    
    # Create sample graph
    astar = create_sample_graph()
    
    # Print graph structure
    astar.print_graph()
    
    # Find path from A to J
    start = "A"
    goal = "J"
    
    print(f"\nFinding path from {start} to {goal}:")
    path = astar.find_path(start, goal)
    
    if path:
        print(f"Path found: {' -> '.join(path)}")
        print(f"Path length: {len(path)} nodes")
        
        # Calculate total cost
        total_cost = 0
        for i in range(len(path) - 1):
            current_node = astar.graph[path[i]]
            next_node_name = path[i + 1]
            total_cost += current_node.neighbors[next_node_name]
        
        print(f"Total cost: {total_cost}")
        
        # Show detailed path with costs
        print("\nDetailed path:")
        for i in range(len(path) - 1):
            current = path[i]
            next_node = path[i + 1]
            cost = astar.graph[current].neighbors[next_node]
            print(f"{current} -> {next_node} (cost: {cost})")
    else:
        print("No path found!")


if __name__ == "__main__":
    main()
