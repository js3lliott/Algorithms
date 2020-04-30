"""
The Dijkstra algorithm takes a graph and a source and returns the minimum distance of each vertex
to that source.
Pre-Conditions: Graph is a list of connections to that vertex and Weight to that vertex in the same order.
                Source is an integer value between 0 to n
                Connections should have n lists inside it similarily for Weights. It can be empty.

Dijkstra(Graph, Source) --> Standard Function Call
"""


def Dijkstra(Graph, Source):

    # Shortest distances to each node
    Short_Distances = []

    # Vertex to be visited are stored here
    Queue_Vertex = []

    # Connections stores connections to each vertex and weights stores the corresponding weight
    Connections = Graph[0]
    Weights = Graph[1]
    Queue_Vertex = list(range(len(Connections)))

    # Setting all distances except source to infinity and source distance to 0
    for Vertex in Queue_Vertex:
        if Vertex == Source:
            Short_Distances.append(0)
        else:
            Short_Distances.append(float('inf'))

    # To visit all Vertices
    while (len(Queue_Vertex) != 0):
        Min_Dist = float('inf')

        # Pick Node with minimum distance currently
        for i in Queue_Vertex:
            if Short_Distances[i] <= Min_Dist:
                Min_Dist = Short_Distances[i]
                Node = i

        # Remove Vertex from Queue as visited
        Queue_Vertex.remove(Node)

        # Set distances of vertices connected to node as minimum
        for Con_Node in Connections[Node]:
            Try_Dist = Short_Distances[Node] + Weights[Node][Connections[Node].index(Con_Node)]
            if Try_Dist <= Short_Distances[Con_Node]:
                Short_Distances[Con_Node] = Try_Dist

    return Short_Distances

# Sample run for example Graph
if __name__=="__main__":
    Test_Graph = [ [[1, 2], [3], [1, 3, 4], [], [3]] , [[ 5, 3], [3], [2, 5, 6], [], [1]] ]
    print(Dijkstra(Test_Graph,0))
    print(Dijkstra(Test_Graph,1))
    print(Dijkstra(Test_Graph,2))
    print(Dijkstra(Test_Graph,3))
    print(Dijkstra(Test_Graph,4))
