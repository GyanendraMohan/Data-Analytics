"""Basic AO* Algorithm"""

graph = {}
costs = {}
heuristics = {}
solved = set()


def add_node(node, h=0):
    graph[node] = []
    costs[node] = []
    heuristics[node] = h


def add_edge(from_node, to_nodes, cost):
    graph[from_node].append(to_nodes)
    costs[from_node].append(cost)


def compute_cost(node):
    if node in solved:
        return 0
    if not graph[node]:
        return heuristics[node]
    min_cost = float('inf')
    for i, child_set in enumerate(graph[node]):
        cost = costs[node][i]
        for child in child_set:
            cost += compute_cost(child)
        min_cost = min(min_cost, cost)
    return min_cost


def ao_star(start):
    # Mark terminal nodes
    for node in graph:
        if not graph[node]:
            solved.add(node)
    
    # Main loop
    for _ in range(50):
        if start in solved:
            return True
        
        # Find best node
        best = None
        best_cost = float('inf')
        for node in graph:
            if node not in solved:
                c = compute_cost(node)
                if c < best_cost:
                    best_cost = c
                    best = node
        
        if not best:
            break
        
        # Solve cheapest path
        min_cost = float('inf')
        best_set = None
        for i, child_set in enumerate(graph[best]):
            cost = costs[best][i]
            for child in child_set:
                if child not in solved:
                    cost += compute_cost(child)
            if cost < min_cost:
                min_cost = cost
                best_set = child_set
        
        if best_set:
            for child in best_set:
                if not graph[child]:
                    solved.add(child)
            # Mark solved nodes
            for node in graph:
                for child_set in graph[node]:
                    if all(c in solved for c in child_set):
                        solved.add(node)
    
    return start in solved


# Example
add_node("A", 5)
add_node("B", 4)
add_node("C", 3)
add_node("D", 2)
add_node("E", 0)
add_node("F", 0)
add_node("G", 0)
add_node("H", 0)

add_edge("A", ["B"], 2)
add_edge("A", ["C"], 3)
add_edge("B", ["D"], 1)
add_edge("C", ["E", "F"], 1)
add_edge("D", ["G"], 2)
add_edge("D", ["H"], 1)

if ao_star("A"):
    print("Solution found!")
    print(f"Solved: {sorted(solved)}")
else:
    print("No solution")
