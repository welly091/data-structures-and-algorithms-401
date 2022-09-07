from data_structures.graph import Graph, Vertex, Edge


def direct_flights(graph, names_list):
    """
    Find the total price for travelling from a start position to the final position.

    :params graph: the map of cities
    :params names_list: a list that contains cities that need to be traveled
    :return: tuple, (boolean, int)
    """
    if len(names_list) == 0:
        return (False, 0)

    final_price = 0
    cities = graph.get_nodes()

    start_index = 0
    end_index = 1

    while end_index < len(names_list):
        start_city = None
        for city in cities:
            if city.value == names_list[start_index]:
                start_city = city

        if start_city is None:
            return (False, 0)

        edges = graph.get_neighbors(start_city)
        checker = False
        for edge in edges:

            if edge.vertex.value == names_list[end_index]:
                final_price += edge.weight
                checker = True
                print(final_price)
        if checker is False:
            return (False, 0)

        start_index +=1
        end_index +=1

    return (True,final_price)




