# Simple BFS algorithm implementation
# Time complexity: O(V + E) where V is the # of nodes and E is the # of edges
# Space complexity: O(V)
import collections

graph = {
    0: [1, 2],
    1: [2],
    2: [3],
    3: [1, 2]
}

def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)
    
    while queue:

        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(vertex)
        # If not visited, mark it as visited and enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


print("Following is Breadth First Traversal: ")
bfs(graph, 0)