import pytest
from data_structures.graph import Graph


def test_exists():
    assert Graph


def test_bfs(graph):
    nodes = graph.get_nodes()
    root = nodes[0]
    print(root.value)
    actual = graph.breadth_first(root)
    expected = ["Pandora", "Arendelle", "Metroville", "Monstropolis", "Narnia", "Naboo"]
    assert actual == expected

    # DANGER: Metroville/Monstropolis could be switched as well as Narnia/Naboo and still be valid BFS. What to do?


@pytest.fixture
def graph():

    realms = Graph()

    pandora = realms.add_node("Pandora")
    arendelle = realms.add_node("Arendelle")
    metroville = realms.add_node("Metroville")
    monstropolis = realms.add_node("Monstropolis")
    narnia = realms.add_node("Narnia")
    naboo = realms.add_node("Naboo")

    realms.add_edge(pandora, arendelle)

    realms.add_edge(arendelle, pandora)
    realms.add_edge(arendelle, metroville)
    realms.add_edge(arendelle, monstropolis)

    realms.add_edge(metroville, arendelle)
    realms.add_edge(metroville, monstropolis)
    realms.add_edge(metroville, narnia)

    realms.add_edge(monstropolis, arendelle)
    realms.add_edge(monstropolis, metroville)
    realms.add_edge(monstropolis, naboo)

    realms.add_edge(narnia, metroville)
    realms.add_edge(narnia, naboo)

    realms.add_edge(naboo, metroville)
    realms.add_edge(naboo, monstropolis)
    realms.add_edge(naboo, narnia)

    return realms


################
### My Tests ###
################

@pytest.fixture
def my_graph():
    g = Graph()
    city_a = g.add_node("Seattle")
    city_b = g.add_node("Boston")
    city_c = g.add_node("Atlanta")
    city_d = g.add_node("Los Angeles")

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

    return g

def test_mytest_1(my_graph):

    nodes = my_graph.get_nodes()
    root = nodes[0]
    actual = my_graph.breadth_first(root)
    expected = ["Seattle", "Boston", "Atlanta", "Los Angeles"]
    assert actual == expected


def test_mytest_2(my_graph):
    nodes = my_graph.get_nodes()
    root = nodes[1]
    actual = my_graph.breadth_first(root)
    expected = ["Boston", "Seattle", "Atlanta", "Los Angeles"]
    assert actual == expected

def test_mytest_3(my_graph):
    my_graph.add_node("New York")
    nodes = my_graph.get_nodes()
    root = nodes[4]
    actual = my_graph.breadth_first(root)
    expected = ["New York"]
    assert actual == expected

def test_mytest_4(my_graph):
    my_graph.add_node("New York")
    nodes = my_graph.get_nodes()
    root = nodes[3]
    actual = my_graph.breadth_first(root)
    expected = ["Los Angeles", "Seattle", "Boston", "Atlanta"]
    assert actual == expected

def test_mytest_5(my_graph):
    my_graph.add_edge(my_graph.add_node("New York"), my_graph.add_node("New Jersey"), 1)
    nodes = my_graph.get_nodes()
    root = nodes[4]
    actual = my_graph.breadth_first(root)
    expected = ["New York", "New Jersey"]
    assert actual == expected
