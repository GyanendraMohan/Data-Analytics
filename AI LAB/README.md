# A\* Algorithm Implementation - Line by Line Guide

## Overview

This implementation provides a complete A* pathfinding algorithm for grid-based navigation with obstacles. The A* algorithm finds the shortest path between two points using a heuristic function to guide the search efficiently.

## Code Structure

### 1. Imports and Dependencies (Lines 1-6)

```python
"""A* Pathfinding Algorithm Implementation"""

import heapq
import math
from typing import List, Tuple, Optional, Set, Dict
from dataclasses import dataclass
```

- `heapq`: For priority queue implementation (open set)
- `math`: For sqrt function in Euclidean distance calculation
- `typing`: For type hints to improve code readability
- `dataclass`: For clean Node class definition

### 2. Node Class (Lines 8-25)

```python
@dataclass
class Node:
    x: int                           # X coordinate in grid
    y: int                           # Y coordinate in grid
    g_cost: float = float('inf')     # Actual cost from start to this node
    h_cost: float = 0.0              # Heuristic cost from this node to goal
    f_cost: float = float('inf')     # Total cost (g_cost + h_cost)
    parent: Optional['Node'] = None  # Parent node for path reconstruction
```

**Key Methods:**

- `__lt__()`: Allows nodes to be compared for priority queue ordering
- `__eq__()`: Enables node equality comparison based on coordinates
- `__hash__()`: Makes nodes hashable for use in sets and dictionaries

### 3. AStar Class Initialization (Lines 28-39)

```python
def __init__(self, grid: List[List[int]], diagonal_movement: bool = True):
    self.grid = grid                 # 2D grid: 0=walkable, 1=obstacle
    self.rows = len(grid)            # Number of rows
    self.cols = len(grid[0]) if self.rows > 0 else 0  # Number of columns
    self.diagonal_movement = diagonal_movement  # Allow diagonal movement?

    if diagonal_movement:
        # 8-directional movement (including diagonals)
        self.directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                         (0, 1), (1, -1), (1, 0), (1, 1)]
    else:
        # 4-directional movement (no diagonals)
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
```

### 4. Validation Method (Lines 41-44)

```python
def is_valid_position(self, x: int, y: int) -> bool:
    return (0 <= x < self.rows and     # Within row bounds
            0 <= y < self.cols and     # Within column bounds
            self.grid[x][y] == 0)      # Not an obstacle
```

### 5. Heuristic Functions (Lines 46-50)

```python
def heuristic_manhattan(self, current: Node, goal: Node) -> float:
    return abs(current.x - goal.x) + abs(current.y - goal.y)

def heuristic_euclidean(self, current: Node, goal: Node) -> float:
    return math.sqrt((current.x - goal.x)**2 + (current.y - goal.y)**2)
```

- **Manhattan**: Sum of horizontal and vertical distances (admissible for 4-directional movement)
- **Euclidean**: Straight-line distance (admissible for diagonal movement)

### 6. Movement Cost Calculation (Lines 52-59)

```python
def get_movement_cost(self, current: Node, neighbor: Node) -> float:
    dx = abs(neighbor.x - current.x)   # Horizontal distance
    dy = abs(neighbor.y - current.y)   # Vertical distance

    if dx == 1 and dy == 1:            # Diagonal movement
        return math.sqrt(2)            # Cost = √2 ≈ 1.414
    else:                              # Horizontal/vertical movement
        return 1.0                     # Cost = 1
```

### 7. Neighbor Discovery (Lines 61-71)

```python
def get_neighbors(self, node: Node) -> List[Node]:
    neighbors = []

    for dx, dy in self.directions:     # Check all possible directions
        new_x, new_y = node.x + dx, node.y + dy  # Calculate new position

        if self.is_valid_position(new_x, new_y):  # If position is valid
            neighbor = Node(new_x, new_y)         # Create neighbor node
            neighbors.append(neighbor)            # Add to neighbors list

    return neighbors
```

### 8. Path Reconstruction (Lines 73-81)

```python
def reconstruct_path(self, goal: Node) -> List[Tuple[int, int]]:
    path = []
    current = goal                    # Start from goal node

    while current is not None:        # Trace back to start
        path.append((current.x, current.y))  # Add current position
        current = current.parent      # Move to parent node

    return path[::-1]                 # Reverse to get start-to-goal path
```

### 9. Main A\* Algorithm (Lines 83-132)

```python
def find_path(self, start: Tuple[int, int], goal: Tuple[int, int],
              heuristic_type: str = 'manhattan') -> Optional[List[Tuple[int, int]]]:
```

#### Initialization (Lines 85-96)

```python
start_node = Node(start[0], start[1])  # Create start node
goal_node = Node(goal[0], goal[1])     # Create goal node

# Validate positions
if not self.is_valid_position(start[0], start[1]) or not self.is_valid_position(goal[0], goal[1]):
    return None

# Select heuristic function
heuristic = self.heuristic_euclidean if heuristic_type == 'euclidean' else self.heuristic_manhattan

# Initialize start node costs
start_node.g_cost = 0                 # Distance from start to start = 0
start_node.h_cost = heuristic(start_node, goal_node)  # Heuristic to goal
start_node.f_cost = start_node.g_cost + start_node.h_cost  # Total cost
```

#### Data Structures Setup (Lines 98-100)

```python
open_set = [start_node]               # Priority queue of nodes to explore
closed_set: Set[Tuple[int, int]] = set()  # Set of explored nodes
all_nodes: Dict[Tuple[int, int], Node] = {(start[0], start[1]): start_node}  # Node lookup
```

#### Main Search Loop (Lines 101-131)

```python
while open_set:                       # While there are nodes to explore
    current = heapq.heappop(open_set) # Get node with lowest f_cost
    closed_set.add((current.x, current.y))  # Mark as explored

    if current == goal_node:          # If we reached the goal
        return self.reconstruct_path(current)  # Return the path

    # Explore all neighbors
    for neighbor_pos in self.get_neighbors(current):
        neighbor_key = (neighbor_pos.x, neighbor_pos.y)

        if neighbor_key in closed_set:  # Skip if already explored
            continue

        # Get or create neighbor node
        if neighbor_key in all_nodes:
            neighbor = all_nodes[neighbor_key]
        else:
            neighbor = Node(neighbor_pos.x, neighbor_pos.y)
            all_nodes[neighbor_key] = neighbor

        # Calculate tentative cost
        movement_cost = self.get_movement_cost(current, neighbor)
        tentative_g_cost = current.g_cost + movement_cost

        # If this path is better than previous path to neighbor
        if tentative_g_cost < neighbor.g_cost:
            neighbor.parent = current                    # Update parent
            neighbor.g_cost = tentative_g_cost           # Update g_cost
            neighbor.h_cost = heuristic(neighbor, goal_node)  # Calculate h_cost
            neighbor.f_cost = neighbor.g_cost + neighbor.h_cost  # Update f_cost

            if neighbor not in open_set:                 # Add to open set if new
                heapq.heappush(open_set, neighbor)

return None  # No path found
```

### 10. Sample Grid Creation (Lines 135-145)

```python
def create_sample_grid() -> List[List[int]]:
    return [
        [0, 0, 0, 1, 0, 0, 0, 0],  # Row 0: 0=walkable, 1=obstacle
        [0, 1, 0, 1, 0, 1, 1, 0],  # Row 1
        [0, 1, 0, 0, 0, 0, 0, 0],  # Row 2
        [0, 0, 0, 1, 1, 1, 0, 1],  # Row 3
        [0, 1, 0, 1, 0, 0, 0, 0],  # Row 4
        [0, 0, 0, 0, 0, 1, 0, 0],  # Row 5
        [0, 1, 1, 1, 0, 1, 0, 0],  # Row 6
        [0, 0, 0, 0, 0, 0, 0, 0]   # Row 7
    ]
```

### 11. Visualization Function (Lines 148-159)

```python
def print_grid_with_path(grid: List[List[int]], path: List[Tuple[int, int]] = None):
    path_set = set(path) if path else set()  # Convert path to set for fast lookup

    for i, row in enumerate(grid):           # Iterate through each row
        for j, cell in enumerate(row):       # Iterate through each column
            if (i, j) in path_set:           # If position is on path
                print("*", end="")           # Print asterisk
            elif cell == 1:                  # If obstacle
                print("█", end="")           # Print filled block
            else:                            # If walkable space
                print(" ", end="")           # Print space
        print()                             # New line after each row
```

### 12. Main Function (Lines 162-171)

```python
def main():
    grid = create_sample_grid()              # Create test grid
    astar = AStar(grid, diagonal_movement=True)  # Initialize A* with diagonal movement
    path = astar.find_path((0, 0), (7, 7), 'manhattan')  # Find path from (0,0) to (7,7)

    if path:                                 # If path found
        print(f"Path found! Length: {len(path)} steps")  # Print path length
        print_grid_with_path(grid, path)     # Visualize path on grid
    else:                                    # If no path found
        print("No path found!")
```

## Algorithm Flow Summary

1. **Initialize**: Create start/goal nodes, set up data structures
2. **Loop**: While open set is not empty:
   - Pop node with lowest f_cost from open set
   - Add to closed set
   - If goal reached, reconstruct and return path
   - For each neighbor:
     - Skip if already in closed set
     - Calculate tentative g_cost
     - If better path found, update neighbor and add to open set
3. **Return**: Path if found, None if no path exists

## Key A\* Formula

```
f(n) = g(n) + h(n)
```

- `f(n)`: Total estimated cost of path through node n
- `g(n)`: Actual cost from start to node n
- `h(n)`: Heuristic estimate of cost from node n to goal

The algorithm is **optimal** (finds shortest path) and **complete** (finds solution if one exists) when using an admissible heuristic.
