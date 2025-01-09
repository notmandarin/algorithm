def build_graph(n, wires):
    graph = [[] for _ in range(n+1)]
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    return graph

def remove_edge(graph, v1, v2):
    graph[v1].remove(v2)
    graph[v2].remove(v1)

def restore_edge(graph, v1, v2):
    graph[v1].append(v2)
    graph[v2].append(v1)

def count_nodes(graph, start, n):
    visited = [False] * (n+1)
    stack = [start]
    visited[start] = True
    count = 1

    while stack:
        node = stack.pop()
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                stack.append(next_node)
                count += 1
    return count

def solution(n, wires):
    graph = build_graph(n, wires)
    answer = float('inf')  

    for v1, v2 in wires:
        remove_edge(graph, v1, v2)

        subtree_count = count_nodes(graph, v1, n)
        other_subtree_count = n - subtree_count

        diff = abs(subtree_count - other_subtree_count)
        answer = min(answer, diff)

        restore_edge(graph, v1, v2)

    return answer
