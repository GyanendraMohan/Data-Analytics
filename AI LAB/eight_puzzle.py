import heapq

class PuzzleNode:
    def __init__(self, node_state, parent_node=None, move=None, cost=0):
        self.node_state = node_state
        self.parent_node = parent_node
        self.move = move
        self.cost = cost
        self.heuristic = self.calculate_heuristic()

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

    def calculate_heuristic(self):
        # Manhattan distance heuristic
        heuristic = 0
        for i in range(3):
            for j in range(3):
                if self.node_state[i][j] != 0:
                    goal_i, goal_j = divmod(self.node_state[i][j] - 1, 3)
                    heuristic += abs(i - goal_i) + abs(j - goal_j)
        return heuristic

def is_valid_move(i, j):
    return 0 <= i < 3 and 0 <= j < 3

def get_neighbors(node):
    neighbors = []
    i, j = next((i, j) for i in range(3) for j in range(3) if node.node_state[i][j] == 0)
    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_i, new_j = i + di, j + dj
        if is_valid_move(new_i, new_j):
            new_state = [row[:] for row in node.node_state]
            new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
            neighbors.append(PuzzleNode(new_state, node, (i, j)))
    return neighbors

def reconstruct_path(node):
    path = []
    while node.parent_node is not None:
        path.append(node)
        node = node.parent_node
    return path[::-1]

def solve_8_puzzle(initial_state):
    start_node = PuzzleNode(initial_state)
    open_set = [start_node]
    heapq.heapify(open_set)
    closed_set = set()

    while open_set:
        current_node = heapq.heappop(open_set)
        if current_node.node_state == goal_state:
            return reconstruct_path(current_node)
        
        closed_set.add(tuple(map(tuple, current_node.node_state)))
        for neighbor in get_neighbors(current_node):
            if tuple(map(tuple, neighbor.node_state)) not in closed_set:
                heapq.heappush(open_set, neighbor)
    
    return None

def parse_input(file_path):
    """
    Parse a file containing 9 integers (0-8) separated by whitespace or newlines into a 3x3 list.
    Example file contents:
    1 2 3
    4 5 6
    7 8 0
    """
    with open(file_path, "r") as f:
        tokens = f.read().split()
    if len(tokens) != 9:
        raise ValueError(f"Expected 9 numbers in {file_path}, got {len(tokens)}")
    nums = [int(t) for t in tokens]
    return [nums[i*3:(i+1)*3] for i in range(3)]

if __name__ == "__main__":
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Define the goal state
    initial_state = parse_input("__ed_input.txt")  # Parse initial state from __ed_input.txt
    path = solve_8_puzzle(initial_state)
    if path:
        print("Solution found! Moves to reach goal state:")
        for move in path:
            print(move.node_state)
    else:
        print("No solution found.")