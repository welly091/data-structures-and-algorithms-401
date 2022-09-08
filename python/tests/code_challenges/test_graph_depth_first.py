import pytest
from data_structures.graph import Graph, Vertex



def test_full(graph_and_root):
    graph, root = graph_and_root
    actual = graph.depth_first_search(root)

    expected = ["a", "b", "c", "g", "d", "e", "h", "f"]
    assert actual == expected



def test_empty():
    graph = Graph()
    node = Vertex("some other node")
    actual = graph.depth_first_search(node)
    expected = []
    assert actual == expected



def test_island_empty():
    graph = Graph()
    lonely = graph.add_node("lonely")
    actual = graph.depth_first_search(lonely)
    expected = ["lonely"]
    assert actual == expected



def test_island_crowded(graph):
    lonely = graph.add_node("lonely")
    actual = graph.depth_first_search(lonely)
    expected = ["lonely"]
    assert actual == expected



def test_mates_crowded(graph):
    lady = graph.add_node("lady")
    the_tramp = graph.add_node("the tramp")
    graph.add_edge(lady, the_tramp, 10)
    graph.add_edge(the_tramp, lady, 10)
    actual = graph.depth_first_search(lady)
    expected = ["lady", "the tramp"]
    assert actual == expected


@pytest.fixture
def graph():

    letters = Graph()

    a = letters.add_node("a")
    b = letters.add_node("b")
    c = letters.add_node("c")
    d = letters.add_node("d")
    e = letters.add_node("e")
    f = letters.add_node("f")
    g = letters.add_node("g")
    h = letters.add_node("h")

    letters.add_edge(a, b)
    letters.add_edge(b, c)
    letters.add_edge(c, g)
    letters.add_edge(a, d)

    letters.add_edge(d, e)
    letters.add_edge(d, h)
    letters.add_edge(d, f)

    letters.add_edge(h, f)

    return letters


@pytest.fixture
def graph_and_root(graph):
    return graph, graph.get_nodes()[0]

##################
#### My tests ####
##################

@pytest.fixture
def my_graph():
    g = Graph()
    city_a = g.add_node("Seattle")
    city_b = g.add_node("Boston")
    city_c = g.add_node("Atlanta")
    city_d = g.add_node("Los Angeles")
    city_e = g.add_node("Denver")
    city_f = g.add_node("Houston")

    g.add_edge(city_a, city_a, 0)
    g.add_edge(city_a, city_b, 9)
    g.add_edge(city_a, city_c, 8)
    g.add_edge(city_a, city_d, 5)

    g.add_edge(city_b, city_a, 9)
    g.add_edge(city_b, city_b, 0)
    g.add_edge(city_b, city_c, 4)
    g.add_edge(city_b, city_d, 10)

    g.add_edge(city_c, city_a, 8)
    g.add_edge(city_c, city_b, 4)
    g.add_edge(city_c, city_c, 0)
    g.add_edge(city_c, city_d, 7)

    g.add_edge(city_d, city_a, 5)
    g.add_edge(city_d, city_b, 10)
    g.add_edge(city_d, city_c, 7)
    g.add_edge(city_d, city_d, 0)
    g.add_edge(city_d, city_e, 4)

    g.add_edge(city_e, city_f, 5)


    return g

def test_mytest_1(my_graph):
    nodes = my_graph.get_nodes()
    city = nodes[0]
    actual = my_graph.depth_first_search(city)
    expected = ["Seattle", "Boston", "Atlanta", "Los Angeles", "Denver", "Houston"]
    assert actual == expected

def test_mytest_2(my_graph):
    nodes = my_graph.get_nodes()
    city = nodes[1]
    actual = my_graph.depth_first_search(city)
    expected = [ "Boston","Seattle", "Atlanta", "Los Angeles", "Denver", "Houston" ]
    assert actual == expected

def test_mytest_3(my_graph):
    nodes = my_graph.get_nodes()
    city = nodes[3]
    actual = my_graph.depth_first_search(city)
    expected = ["Los Angeles", "Seattle", "Boston", "Atlanta", "Denver", "Houston" ]
    assert actual == expected

def test_mytest_4(my_graph):
    nodes = my_graph.get_nodes()
    city = nodes[-2] #"Denver
    city_houston = nodes[-1] #Houston
    city_london = my_graph.add_node("London")
    city_beijing = my_graph.add_node("Beijing")
    city_tokyo = my_graph.add_node("Tokyo")

    my_graph.add_edge(city, city_london , 100) #Denver --100---> London
    my_graph.add_edge(city_london, city_beijing, 1000) # Denver --100---> London --1000---> Beijing
    my_graph.add_edge(city_houston, city_tokyo, 1300) # Denver --5--> Houston --1300---> Tokyo
    actual = my_graph.depth_first_search(city)
    expected = ["Denver", "Houston", "Tokyo", "London", "Beijing"]
    assert actual == expected
