from collections import deque

def main(graph, start_node, end_node):
    visited = set()
    queue = deque([(start_node, [start_node])])

    while queue:
        node, path = queue.popleft()
        if node == end_node:
            print("Shortest path:", ' -> '.join(map(str, path)))
            return
        if node not in visited:
            visited.add(node)
            for child in graph.get(node, []):
                if child not in visited:
                    new_path = path + [child]
                    queue.append((child, new_path))


nodes = {
    1: [2, 3, 4],
    2: [1, 5, 6, 7, 8],
    3: [1, 8, 9, 4],
    4: [1, 3, 10, 11],
    5: [2],
    6: [2, 12],
    7: [13, 14, 16],
    8: [2, 3, 9, 15, 17, 16],
    9: [3, 8, 18],
    10: [4, 18],
    11: [19, 20],
    12: [6, 13],
    13: [7, 12],
    14: [7],
    15: [8, 16],
    16: [7, 8, 15],
    17: [8],
    18: [9, 10],
    19: [11],
    20: [11]
}

start_node = 16
end_node = 20

print("BFS Shortest Path:")
main(nodes, start_node, end_node)