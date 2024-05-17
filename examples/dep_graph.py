class Graph:
    def __init__(self, node_names: list):
        self.graph = {node: [] for node in node_names}

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, node, visited, stack):
        visited[node] = True

        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, stack)

        stack.append(node)

    def topological_sort(self):
        visited = {node: False for node in self.graph}
        stack = []

        for node in self.graph:
            if not visited[node]:
                self.dfs(node, visited, stack)

        return stack[::-1]

def evaluate_operations(dependency_graph):
    graph = Graph(dependency_graph.keys())
    for node, dependencies in dependency_graph.items():
        for dependency in dependencies:
            graph.add_edge(dependency, node)

    evaluation_order = graph.topological_sort()

    # Assign numbers to nodes based on their dependencies
    node_numbers = {}
    max_number = 0
    for node in evaluation_order:
        if not dependency_graph[node]:
            node_numbers[node] = 1
        else:
            node_numbers[node] = max([node_numbers[dep] for dep in dependency_graph[node]]) + 1
        max_number = max(max_number, node_numbers[node])

    # Group nodes based on their numbers for parallel evaluation
    parallel_evaluation = [[] for _ in range(max_number)]
    for node, number in node_numbers.items():
        parallel_evaluation[number - 1].append(node)

    return parallel_evaluation

# Example usage:
dependency_graph = {
    'A': [],
    'B': ['A'],
    'C': ['A'],
    'D': ['B', 'C'],
    'E': ['D']
}

parallel_evaluation = evaluate_operations(dependency_graph)
print("Parallel evaluation groups:", parallel_evaluation)
