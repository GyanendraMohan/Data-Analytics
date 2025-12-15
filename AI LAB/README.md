# AI LAB Experiments

This folder contains Python implementations of foundational algorithms and classic problems for Artificial Intelligence/Data Structures and Algorithms laboratory courses. The code serves for educational experimentation, learning, and assignments.

---

## Contents

- **Search algorithms:** A\*, BFS, DFS
- **Minimum Spanning Tree:** Prim's, Kruskal's
- **Shortest Path:** Dijkstra
- **Classic Problems:** 8-Queens, 8-Puzzle (A\* and BFS)
- **Sorting:** Merge Sort, Quick Sort
- **Graph Analysis:** Biconnected components, articulation points
- **Data Structures:** Binary Search Tree (traversals)
- **Other:** Custom A\* on graphs with heuristics

---

## Theory

### Breadth-First Search (BFS)

**Overview:** BFS is a graph traversal algorithm that explores all vertices at the current depth level before moving to the next level. It uses a queue data structure (FIFO - First In First Out).

**Key Concepts:**

- Explores nodes level by level
- Guarantees shortest path in unweighted graphs
- Uses a queue to maintain frontier of nodes to visit
- Marks visited nodes to avoid cycles

**Time Complexity:** O(V + E) where V = vertices, E = edges  
**Space Complexity:** O(V) for the queue and visited set

**Applications:** Shortest path in unweighted graphs, level-order traversal, social networking, web crawling

---

### A\* Search Algorithm

**Overview:** A\* is an informed search algorithm that finds the shortest path from a start node to a goal node by using both the actual cost from start (g(n)) and an admissible heuristic estimate to goal (h(n)). The evaluation function is f(n) = g(n) + h(n).

**Key Concepts:**

- **Admissible Heuristic:** h(n) never overestimates the true cost to the goal
- **Optimality:** Guarantees optimal solution if heuristic is admissible
- Uses priority queue (min-heap) to explore nodes with lowest f(n) first
- Combines best of Dijkstra's algorithm (guaranteed optimal) and Greedy Best-First Search (efficient)

**Time Complexity:** O(b^d) worst case, where b = branching factor, d = depth  
**Space Complexity:** O(b^d) for storing all nodes in memory

**Heuristics:**

- **Manhattan Distance:** Sum of horizontal and vertical distances |x1-x2| + |y1-y2|
- **Euclidean Distance:** Straight-line distance √((x1-x2)² + (y1-y2)²)

**Applications:** Pathfinding in games, GPS navigation, robotics, AI planning

---

### Depth-First Search (DFS)

**Overview:** DFS explores as far as possible along each branch before backtracking. It uses a stack (or recursion) to maintain the path.

**Key Concepts:**

- Explores deep into the graph before backtracking
- Uses stack (LIFO) or recursion
- Can find cycles, topological sorting
- Memory efficient compared to BFS for deep graphs

**Time Complexity:** O(V + E)  
**Space Complexity:** O(V) for recursion stack

**Applications:** Cycle detection, topological sorting, maze solving, puzzle games

---

### Dijkstra's Algorithm

**Overview:** Dijkstra's algorithm finds the shortest path from a source vertex to all other vertices in a weighted graph with non-negative edge weights. It's a greedy algorithm.

**Key Concepts:**

- Maintains distance estimates and progressively relaxes edges
- Uses priority queue to select vertex with minimum distance
- **Greedy Choice:** Always picks unvisited vertex with smallest known distance
- Cannot handle negative edge weights (use Bellman-Ford for that)

**Time Complexity:** O((V + E) log V) with binary heap, O(V²) with array  
**Space Complexity:** O(V)

**Applications:** Network routing, GPS navigation, social network analysis, game development

---

### Prim's Algorithm

**Overview:** Prim's algorithm finds a Minimum Spanning Tree (MST) for a weighted undirected graph. It grows the MST by adding the minimum-weight edge that connects a vertex in the MST to a vertex outside.

**Key Concepts:**

- Greedy algorithm: at each step, adds minimum-weight edge
- Maintains two sets: vertices in MST and vertices not yet included
- Starts from an arbitrary vertex
- Ensures no cycles are created

**Time Complexity:** O(V²) with adjacency matrix, O((V + E) log V) with adjacency list and binary heap  
**Space Complexity:** O(V)

**Applications:** Network design, clustering, image segmentation, approximation algorithms

---

### Kruskal's Algorithm

**Overview:** Kruskal's algorithm finds an MST by sorting all edges by weight and adding them in increasing order, avoiding cycles using Union-Find (Disjoint Set Union).

**Key Concepts:**

- Sorts edges by weight (greedy approach)
- Uses Union-Find data structure to detect cycles
- Adds edges that don't form cycles
- Can process edges in parallel (unlike Prim's)

**Time Complexity:** O(E log E) = O(E log V) due to sorting  
**Space Complexity:** O(V) for Union-Find data structure

**Union-Find (DSU):**

- **Find:** Determines which subset an element belongs to
- **Union:** Joins two subsets into one
- Uses path compression and union by rank for optimization

**Applications:** Network design, clustering, minimum spanning tree problems

---

### Merge Sort

**Overview:** Merge Sort is a divide-and-conquer sorting algorithm that divides the array into halves, recursively sorts them, and merges the sorted halves.

**Key Concepts:**

- **Divide:** Split array into two halves
- **Conquer:** Recursively sort both halves
- **Combine:** Merge the two sorted halves
- Stable sorting algorithm (maintains relative order of equal elements)
- Guaranteed O(n log n) performance

**Time Complexity:** O(n log n) in all cases  
**Space Complexity:** O(n) for temporary arrays

**Merging Process:**

- Compare elements from both halves
- Copy smaller element to result
- Continue until one half is exhausted
- Copy remaining elements

**Applications:** External sorting, stable sorting requirements, linked list sorting

---

### Quick Sort

**Overview:** Quick Sort is a divide-and-conquer algorithm that picks a pivot element, partitions the array around the pivot, and recursively sorts subarrays.

**Key Concepts:**

- **Pivot Selection:** Choose an element as pivot (first, last, median, random)
- **Partitioning:** Rearrange array so elements < pivot are on left, > pivot on right
- **Recursion:** Recursively sort left and right subarrays
- In-place sorting (minimal extra memory)
- Average case is very fast, but worst case is O(n²)

**Time Complexity:**

- Best/Average: O(n log n)
- Worst: O(n²) when pivot is always smallest/largest
  **Space Complexity:** O(log n) for recursion stack (average case)

**Optimizations:**

- Randomized pivot selection
- Median-of-three pivot
- Tail recursion elimination
- Hybrid with insertion sort for small subarrays

**Applications:** General-purpose sorting, in-place sorting requirements, library implementations

---

### Binary Search Tree Traversals

**Overview:** Tree traversal is visiting all nodes in a tree exactly once. Three main recursive traversals differ in the order of visiting root, left subtree, and right subtree.

**Key Concepts:**

1. **Preorder (Root-Left-Right):**

   - Visit root first
   - Then left subtree
   - Then right subtree
   - Used for copying trees, prefix expressions

2. **Inorder (Left-Root-Right):**

   - Visit left subtree first
   - Then root
   - Then right subtree
   - For BST: gives sorted order of elements

3. **Postorder (Left-Right-Root):**
   - Visit left subtree first
   - Then right subtree
   - Then root
   - Used for deleting trees, postfix expressions

**Time Complexity:** O(n) where n = number of nodes  
**Space Complexity:** O(h) where h = height of tree (for recursion stack)

**Applications:** Expression evaluation, tree deletion, copying trees, generating sorted lists

---

### N-Queens Problem

**Overview:** The N-Queens problem is placing N chess queens on an N×N board such that no two queens attack each other (no two queens share same row, column, or diagonal).

**Key Concepts:**

- Uses **backtracking** (systematic search with constraint checking)
- **Constraint Satisfaction:** Queens must not attack each other
- **Pruning:** Abandon partial solutions that violate constraints
- **Recursion:** Try placing queen in each column of current row

**Algorithm Steps:**

1. Start with first row
2. Try placing queen in each column
3. Check if placement is safe (no conflicts)
4. If safe, recursively place queen in next row
5. If no safe placement, backtrack to previous row

**Time Complexity:** O(N!) worst case, but pruning makes it much better  
**Space Complexity:** O(N) for recursion stack and solution storage

**Applications:** Constraint satisfaction problems, scheduling, resource allocation, puzzle solving

---

### Biconnected Components & Articulation Points

**Overview:** An articulation point (cut vertex) is a vertex whose removal increases the number of connected components. A biconnected component is a maximal biconnected subgraph.

**Key Concepts:**

**Articulation Point:**

- Vertex whose removal disconnects the graph
- Critical points in network reliability
- A vertex v is an articulation point if:
  - It's root and has ≥2 children in DFS tree, OR
  - It's not root and has a child with no back edge to ancestor of v

**Biconnected Component:**

- Maximal set of edges such that any two edges lie on a common simple cycle
- Removing any one vertex doesn't disconnect the component
- Used in network design and fault tolerance

**Tarjan's Algorithm:**

- Uses DFS with discovery time (disc) and low link values
- **Discovery Time:** When vertex is first visited
- **Low Link:** Earliest discovery time reachable from subtree

**Time Complexity:** O(V + E)  
**Space Complexity:** O(V + E)

**Applications:** Network reliability analysis, critical infrastructure identification, social network analysis

---

### 8-Puzzle Problem

**Overview:** The 8-puzzle is a sliding puzzle with 8 numbered tiles and one empty space on a 3×3 grid. Goal is to rearrange tiles from initial state to goal state [[1,2,3],[4,5,6],[7,8,0]].

**Key Concepts:**

- **State Space Search:** Each puzzle configuration is a state
- **Valid Moves:** Slide tile into empty space (4 possible moves: up, down, left, right)
- **Solvability:** Only half of all possible configurations are solvable
- Can be solved using BFS (optimal but slow) or A\* (optimal and faster with heuristic)

**Solvability Check:**

- Count inversions (pairs of tiles (a,b) where a > b and a appears before b)
- Puzzle is solvable if number of inversions is even (for goal state with empty at bottom-right)

**Heuristics for A\*:**

- **Manhattan Distance:** Sum of distances each tile is from its goal position
- **Hamming Distance:** Number of misplaced tiles
- Manhattan distance is more informed and leads to faster search

**Time Complexity:**

- BFS: O(b^d) where b = branching factor (≈3), d = depth
- A\*: O(b^d*) where d* = depth of optimal solution (much better with good heuristic)

**Applications:** AI search algorithms, puzzle solving, pathfinding variations, algorithm demonstrations

---

## Experiment Scripts

### 1. `eight_puzzle_basic.py`

- **Algorithm:** Breadth-First Search (BFS)
- **Purpose:** Solves the 8-puzzle by finding the shortest path.
- **Theory:** See **8-Puzzle Problem** and **Breadth-First Search** sections above.
- **How to Run:**
  ```bash
  python3 eight_puzzle_basic.py
  ```
- **Config:** Edit `initial_state` in the script for new puzzles.

### 2. `eight_puzzle.py`

- **Algorithm:** A\* Search
- **Purpose:** Solves the 8-puzzle efficiently using Manhattan heuristic.
- **Theory:** See **A\* Search Algorithm** and **8-Puzzle Problem** sections above.
- **How to Run:**
  1. Create an input file, e.g. `__ed_input.txt`:
     ```
     1 2 3
     4 0 6
     7 5 8
     ```
  2. Run:
     ```bash
     python3 eight_puzzle.py
     ```

### 3. `astar.py`

- **Algorithm:** A\* Search (2D grid, supports diagonals)
- **Purpose:** Finds shortest paths on a grid/pathfinding demo with obstacles.
- **Theory:** See **A\* Search Algorithm** section above. This implementation uses both Manhattan and Euclidean heuristics, and supports 8-directional movement.
- **How to Run:**
  ```bash
  python3 astar.py
  ```
- **Config:** Edit the grid/obstacles in `create_sample_grid()` function.

### 4. `bfs.py`

- **Algorithm:** BFS & DFS on graphs
- **Purpose:** Demonstrates BFS and DFS traversals; checks graph connectivity.
- **Theory:** See **Breadth-First Search** and **Depth-First Search** sections above.
- **How to Run:**
  ```bash
  python3 bfs.py
  ```
- **Config:** Edit the `graph` dictionary to test with different graphs.

### 5. `eight_queens.py`

- **Algorithm:** N-Queens (Backtracking)
- **Purpose:** Prints all solutions for placing N (default 4) queens on an N×N board.
- **Theory:** See **N-Queens Problem** section above. Demonstrates constraint satisfaction and backtracking.
- **How to Run:**
  ```bash
  python3 eight_queens.py
  ```
- **Config:** Change `nQueens(N)` for different board sizes (e.g., 4, 8).

### 6. `biconnected.py`

- **Algorithms:** Tarjan's for articulation points & biconnected components
- **Purpose:** Finds critical vertices (articulation points) and maximal biconnected subgraphs.
- **Theory:** See **Biconnected Components & Articulation Points** section above. Uses DFS with discovery time and low link values.
- **How to Run:**
  ```bash
  python3 biconnected.py
  ```

### 7. `dijkstra.py`

- **Algorithm:** Dijkstra's Shortest Path (Adjacency Matrix)
- **Purpose:** Computes shortest path from a source vertex to all vertices in a weighted graph.
- **Theory:** See **Dijkstra's Algorithm** section above. This implementation uses adjacency matrix representation.
- **How to Run:**
  ```bash
  python3 dijkstra.py
  ```
- **Config:** Edit the `g.graph` adjacency matrix to test with different graphs.

### 8. `kruskal.py`

- **Algorithm:** Kruskal's Minimum Spanning Tree
- **Purpose:** Finds the MST for a given edge-weighted undirected graph using Union-Find.
- **Theory:** See **Kruskal's Algorithm** section above. Demonstrates greedy approach with cycle detection using Disjoint Set Union (DSU).
- **How to Run:**
  ```bash
  python3 kruskal.py
  ```
- **Config:** Add/remove edges using `add_edges()` method in the script.

### 9. `mergesort.py`

- **Algorithm:** Merge Sort (recursive)
- **Purpose:** Demonstrates classic divide-and-conquer sorting algorithm.
- **Theory:** See **Merge Sort** section above. Guaranteed O(n log n) time complexity, stable sort.
- **How to Run:**
  ```bash
  python3 mergesort.py
  ```
- **Config:** Change the input array in the `if __name__ == "__main__"` block.

### 10. `binarysearch.py`

- **Algorithm:** Binary Search Tree traversals
- **Purpose:** Shows preorder, inorder, and postorder traversals on a sample BST.
- **Theory:** See **Binary Search Tree Traversals** section above. Demonstrates three fundamental tree traversal techniques.
- **How to Run:**
  ```bash
  python3 binarysearch.py
  ```
- **Config:** Edit tree structure by modifying the `Node` creation code.

### 11. `prims.py`

- **Algorithm:** Prim's Minimum Spanning Tree
- **Purpose:** Finds the MST in an adjacency matrix graph using greedy approach.
- **Theory:** See **Prim's Algorithm** section above. Grows MST by adding minimum-weight edges.
- **How to Run:**
  ```bash
  python3 prims.py
  ```
- **Config:** Modify graph matrices in test functions or use interactive mode.

### 12. `quicksort.py`

- **Algorithm:** Quick Sort (recursive, measures execution time)
- **Purpose:** Classic sorting demo with performance timing.
- **Theory:** See **Quick Sort** section above. Divide-and-conquer with pivot partitioning. Average case O(n log n).
- **How to Run:**
  ```bash
  python3 quicksort.py
  ```
- **Config:** Edit input array in the `if __name__ == "__main__"` block.

### 13. `astar_basic.py`

- **Algorithm:** Basic A\* (manual node/edge/heuristic demo)
- **Purpose:** Shows A\* on a custom-built graph with manual heuristics and node connections.
- **Theory:** See **A\* Search Algorithm** section above. Educational implementation showing A\* fundamentals on a graph structure.
- **How to Run:**
  ```bash
  python3 astar_basic.py
  ```
- **Config:** Edit graph structure and heuristics in `create_sample_graph()` function.

---

## How to Add New Experiments

1. Create a new `.py` file.
2. Add a docstring at top describing the main algorithm/problem solved.
3. Document how to run the file in this README (see above for format).

## Requirements

- Most scripts require Python 3.6+ (standard library only).
- If your experiment needs third-party libraries, mention them at top and in `requirements.txt` (if present).

---

## Contact

For queries, improvement suggestions, or error reports, reach out to the project maintainer, instructor, or your lab teaching assistant.

## AI Definition

Standard definition of Artificial Intelligence (AI):

Artificial Intelligence is the branch of computer science that deals with creating systems capable of performing tasks that normally require human intelligence, such as learning, reasoning, problem-solving, perception, and decision-making.
