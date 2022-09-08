from data_structures.queue import Queue
from data_structures.stack import Stack

class Graph:
    """
    Graph class allows you to add vertices or edges, to get all nodes, and to retrieve a specific vertice's neighbors.
    """

    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, value):
        """
        Takes in a value of any type, adds to the graph, and return the vertex class with the value.

        :params value: any type
        :return : vertex class
        """
        vertex = Vertex(value)

        #get the vertex/node IN the graph
        self.adjacency_list[vertex] = []

        return vertex

    def size(self):
        """
        Return how many vertexes are there in the graph

        :return: None
        """

        return len(self.adjacency_list)

    def get_nodes(self):
        """
        Return all vertex instances stored inside the graph

        :return: dict_key list
        """
        #If the graph is empty, return None
        if list(self.adjacency_list.keys()) == []:
            return None
        return list(self.adjacency_list.keys())

    def add_edge(self, start_vertex, end_vertex, weight=0):
        """
        Add a weighted/unweighted edge between two vertexes.

        :params start_vertex: the vertex that connects
        :params end_vertex: the vertex that is being connected to
        :weight: the weight of the edge
        :return : None
        """
        edge = Edge(end_vertex, weight)

        if end_vertex not in self.adjacency_list:
            raise KeyError

        self.adjacency_list[start_vertex].append(edge)

    def get_neighbors(self, vertex):
        """
        Get all neighbor vertexes associated with a given vertex

        :params vertex: searching this vertex's neighbors
        :return: list of the neighbors of a vertex
        """
        return list(self.adjacency_list[vertex])

    def breadth_first(self, vertex):
        """
        Start with the given vertex to find all connected vertexes using breadth-first search algorithm.

        :params vertex: vertex started from
        :return: list, list of vertexes
        """
        nodes = []
        breadth_queue = Queue()
        visited = set()

        breadth_queue.enqueue(vertex)
        visited.add(vertex)

        while not breadth_queue.is_empty():
            front = breadth_queue.dequeue()
            nodes.append(front.value)

            for each_edge in self.get_neighbors(front):
                if each_edge.vertex not in visited:
                    visited.add(each_edge.vertex)
                    breadth_queue.enqueue(each_edge.vertex)

        return nodes

    def depth_first_search(self, vertex):
        """
        Start with the given vertex to find all connected vertexes using depth-first search algorithm in preorder traversal.

        :params vertex: vertex started from
        :return: list, list of vertexes
        """
        if self.get_nodes() is None:
            return []

        nodes = []
        depth_stack = Stack()
        visited = set()

        depth_stack.push(vertex)
        visited.add(vertex)

        while not depth_stack.is_empty():
            front = depth_stack.pop()
            nodes.append(front.value)

            for each_edge in self.get_neighbors(front)[::-1]:
                if each_edge.vertex not in visited:
                    visited.add(each_edge.vertex)
                    depth_stack.push(each_edge.vertex)

        return nodes


class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
