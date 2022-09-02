# Code Challenge: Class 35: Graph Implementation
# Hashtables
A graph is a non-linear data stucture that as a collection of **vertices**, or a node,
and each vertice potentially connects with other vertices with weighted or unweighted **edges**.
Graph is implemented for many purposes like GPS, mapping, social networks, etc.

## Challenge
All tests for this challenge should be passed.

## Approach & Efficiency
Set up multiple APIs for Graph.
The Big(O) for time complexity for getting all vertices is O(1).
The Big(O) for space complexity is O(N), where N is determined by how many vertices are stored.

## API

[Graph_class](../../data_structures/graph.py)
- **add_node(value)**: Takes in a value of any type, adds to the graph, and return the vertex class with the value
- **size()**: Return how many vertexes are there in the graph
- **get_nodes()**: Return all vertex instances stored inside the graph
- **add_edge(start_vertex, end_vertex, weight=0)**: Add a weighted/unweighted edge between two vertexes. Default for weight is 0.
- **get_neighbors(vertex)**: Get all neighbor vertexes associated with a given vertex

## Testing

Go to [test_graph](../../tests/data_structures/test_graph.py) and run ``pytest``.

