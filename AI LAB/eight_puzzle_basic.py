from collections import deque

# The goal state for reference
GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]   # 0 represents the empty space
]

# Movements: up, down, left, right
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def print_state(state):
    for row in state:
        print(' '.join(str(num) for num in row))
    print()

def get_neighbors(state):
    neighbors = []
    # Find the empty position (0)
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j
    for dx, dy in DIRECTIONS:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            # Create a copy and swap
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def state_to_tuple(state):
    return tuple(tuple(row) for row in state)

def bfs(initial_state):
    queue = deque()
    queue.append((initial_state, []))
    visited = set()
    visited.add(state_to_tuple(initial_state))
    
    while queue:
        current, path = queue.popleft()
        if current == GOAL_STATE:
            return path + [current]
        for neighbor in get_neighbors(current):
            tuple_neighbor = state_to_tuple(neighbor)
            if tuple_neighbor not in visited:
                visited.add(tuple_neighbor)
                queue.append((neighbor, path + [current]))
    return None

if __name__ == "__main__":
    # Example initial state (solvable)
    initial_state = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]

    solution = bfs(initial_state)
    if solution:
        print(f"Solution found in {len(solution) - 1} moves:")
        for step in solution:
            print_state(step)
    else:
        print("No solution found.")
