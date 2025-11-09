import numpy as np

def compute_pagerank_once(matrix, vector, damping=0.85):
    size = len(matrix)
    transition = matrix / matrix.sum(axis=0, keepdims=True)
    transition = np.nan_to_num(transition)
    updated = damping * transition.dot(vector) + (1 - damping) / size
    return updated

def pagerank_iterations(matrix, vector, iters):
    for _ in range(iters):
        vector = compute_pagerank_once(matrix, vector)
    return vector

def pagerank_converge(matrix, vector, threshold=1e-6, max_loops=1000):
    for i in range(max_loops):
        new_vector = compute_pagerank_once(matrix, vector)
        if np.abs(new_vector - vector).sum() < threshold:
            print(f"Converged in {i+1} steps.")
            return new_vector
        vector = new_vector
    print("No convergence within limit.")
    return vector

def uniform_start(size):
    print("Uniform initialization chosen.")
    return np.full(size, 1/size)

print("PAGE RANK ROUTINE")
nodes = int(input("Total nodes: "))

print("Input rows for adjacency matrix, space-separated:")
adjacency = [list(map(int, input(f"Row {i+1}: ").split())) for i in range(nodes)]
adjacency = np.array(adjacency, float)

rank_vector = uniform_start(nodes)

print("Choose mode:\n1. Fixed iterations\n2. Until convergence")
choice = int(input("Mode (1 or 2): "))

if choice == 1:
    steps = int(input("Number of iterations: "))
    result = pagerank_iterations(adjacency, rank_vector, steps)
    print("Rank vector after steps:\n", result)
elif choice == 2:
    tol = float(input("Tolerance (e.g., 1e-6): "))
    result = pagerank_converge(adjacency, rank_vector, tol)
    print("Final converged rank vector:\n", result)
else:
    print("Invalid mode selected.")
