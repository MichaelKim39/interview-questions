from collections import defaultdict
from collections import deque


class Graph:
    def __init__(self):
        self.nodes = defaultdict(list)

    def addEdge(self, u, v):
        self.nodes[u].append(v)

    def printBFS(self, source):
        # Mark all nodes as not visited
        visited = [False] * len(self.nodes)
        # Create queue
        queue = deque()
        # Visit source node and enqueue
        queue.append(source)
        visited[source] = True
        #
        while queue:
            # Dequeue node and print
            current = queue.popleft()
            print(node)
            # Get all adjacent vertices
            # Visit and enqueue all unvisited vertices
            for neighbour in self.nodes[current]:
                if visited[neighbour] == False:
                    queue.append(neighbour)
                    visited[neighbour] = True

    def printDFS(self, source):
        # Mark all nodes as not visited
        visited = [False] * len(self.nodes)
        # Call recursive helper function
        self.DFSUtil(source, visited)

    def DFSUtil(self, node, visited):
        # Visit and print node
        visited[node] = True
        print(node)
        # Recur for all adjacent vertices
        for neighbour in self.nodes[node]:
            if visited[neighbour] == False:
                self.DFSUtil(neighbour, visited)


class Node:
    def __init(self, data):
        self.data = data
        self.adjacent = defaultdict(list)


def main():
    print("Main Function")

    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is DFS from (starting from vertex 2)")
    g.printDFS(2)


if __name__ == '__main__':
    main()
