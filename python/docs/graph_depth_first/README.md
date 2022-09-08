# Code Challenge Class 38
## Graph Depth-first Search
Conduct a depth first preorder traversal on a graph

## Challenge Summary
All tests for this challenge should be passed.

## Whiteboard Process
![depth_first](graph_depth_first.png)

## Approach & Efficiency
- Construct a stack, a set for visited vertexes, and a list for storing the vertexes values
- Traverse the graph
- Store the first vertex into the stack
- Pop from stack and get a vertex
- If the vertex is not visited yet(not in the set), store this vertex value into the list
- Store the vertex into the set and store its children vertexes, starting from most right vertex, into the stack
- Repeat previous three steps until there is no vertex needs to be stored into the stack
- Return the list of vertex values

Big O:

Time complexity: O(N): N is the size of the graph

Space complexity: O(N): N is the size of the graph since we need to store visited vertexes into set.

## Solution
Run the test files for API functions below and check if test cases are all passed.

### API

[graph](../../data_structures/graph.py)
- depth_first_search (vertex): start with the given vertex to find all connected vertexes using depth-first search algorithm.

## Testing

Go to [test_graph_depth_first](../../tests/code_challenges/test_graph_depth_first.py) and run ``pytest``.

