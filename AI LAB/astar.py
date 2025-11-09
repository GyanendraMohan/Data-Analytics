"""A* Pathfinding Algorithm Implementation"""

import heapq
import math
from typing import List, Tuple, Optional, Set, Dict
from dataclasses import dataclass


@dataclass
class Node:
    x: int
    y: int
    g_cost: float = float('inf')
    h_cost: float = 0.0
    f_cost: float = float('inf')
    parent: Optional['Node'] = None
    
    def __lt__(self, other):
        return self.f_cost < other.f_cost
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))


class AStar:
    def __init__(self, grid: List[List[int]], diagonal_movement: bool = True):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.diagonal_movement = diagonal_movement
        
        if diagonal_movement:
            self.directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), 
                             (0, 1), (1, -1), (1, 0), (1, 1)]
        else:
            self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def is_valid_position(self, x: int, y: int) -> bool:
        return (0 <= x < self.rows and 
                0 <= y < self.cols and 
                self.grid[x][y] == 0)
    
    def heuristic_manhattan(self, current: Node, goal: Node) -> float:
        return abs(current.x - goal.x) + abs(current.y - goal.y)
    
    def heuristic_euclidean(self, current: Node, goal: Node) -> float:
        return math.sqrt((current.x - goal.x)**2 + (current.y - goal.y)**2)
    
    def get_movement_cost(self, current: Node, neighbor: Node) -> float:
        dx = abs(neighbor.x - current.x)
        dy = abs(neighbor.y - current.y)
        
        if dx == 1 and dy == 1:
            return math.sqrt(2)
        else:
            return 1.0
    
    def get_neighbors(self, node: Node) -> List[Node]:
        neighbors = []
        
        for dx, dy in self.directions:
            new_x, new_y = node.x + dx, node.y + dy
            
            if self.is_valid_position(new_x, new_y):
                neighbor = Node(new_x, new_y)
                neighbors.append(neighbor)
        
        return neighbors
    
    def reconstruct_path(self, goal: Node) -> List[Tuple[int, int]]:
        path = []
        current = goal
        
        while current is not None:
            path.append((current.x, current.y))
            current = current.parent
        
        return path[::-1]
    
    def find_path(self, start: Tuple[int, int], goal: Tuple[int, int], 
                  heuristic_type: str = 'manhattan') -> Optional[List[Tuple[int, int]]]:
        start_node = Node(start[0], start[1])
        goal_node = Node(goal[0], goal[1])
        
        if not self.is_valid_position(start[0], start[1]) or not self.is_valid_position(goal[0], goal[1]):
            return None
        
        heuristic = self.heuristic_euclidean if heuristic_type == 'euclidean' else self.heuristic_manhattan
        
        start_node.g_cost = 0
        start_node.h_cost = heuristic(start_node, goal_node)
        start_node.f_cost = start_node.g_cost + start_node.h_cost
        
        open_set = [start_node]
        closed_set: Set[Tuple[int, int]] = set()
        all_nodes: Dict[Tuple[int, int], Node] = {(start[0], start[1]): start_node}
        
        while open_set:
            current = heapq.heappop(open_set)
            closed_set.add((current.x, current.y))
            
            if current == goal_node:
                return self.reconstruct_path(current)
            
            for neighbor_pos in self.get_neighbors(current):
                neighbor_key = (neighbor_pos.x, neighbor_pos.y)
                
                if neighbor_key in closed_set:
                    continue
                
                if neighbor_key in all_nodes:
                    neighbor = all_nodes[neighbor_key]
                else:
                    neighbor = Node(neighbor_pos.x, neighbor_pos.y)
                    all_nodes[neighbor_key] = neighbor
                
                movement_cost = self.get_movement_cost(current, neighbor)
                tentative_g_cost = current.g_cost + movement_cost
                
                if tentative_g_cost < neighbor.g_cost:
                    neighbor.parent = current
                    neighbor.g_cost = tentative_g_cost
                    neighbor.h_cost = heuristic(neighbor, goal_node)
                    neighbor.f_cost = neighbor.g_cost + neighbor.h_cost
                    
                    if neighbor not in open_set:
                        heapq.heappush(open_set, neighbor)
        
        return None


def create_sample_grid() -> List[List[int]]:
    return [
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 1],
        [0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]


def print_grid_with_path(grid: List[List[int]], path: List[Tuple[int, int]] = None):
    path_set = set(path) if path else set()
    
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if (i, j) in path_set:
                print("*", end="")
            elif cell == 1:
                print("█", end="")
            else:
                print(" ", end="")
        print()


def main():
    grid = create_sample_grid()
    astar = AStar(grid, diagonal_movement=True)
    path = astar.find_path((0, 0), (7, 7), 'manhattan')
    
    if path:
        print(f"Path found! Length: {len(path)} steps")
        print_grid_with_path(grid, path)
    else:
        print("No path found!")


if __name__ == "__main__":
    main()
