import pytest
from data_structures.graph import Graph
from code_challenges.graph_business_trip import direct_flights



def test_metroville_pandora(planets):
    names = ["Metroville", "Pandora"]
    assert direct_flights(planets, names) == (True, 82)



def test_metroville_monstropolis(planets):
    names = ["Metroville", "New Monstropolis"]
    assert direct_flights(planets, names) == (True, 105)



def test_arendelle_monstropolis_naboo(planets):
    names = ["Arendelle", "New Monstropolis", "Naboo"]
    assert direct_flights(planets, names) == (True, 115)



def test_naboo_pandora(planets):
    names = ["Naboo", "Pandora"]
    assert direct_flights(planets, names) == (False, 0)



def test_narnia_arendelle_naboo(planets):
    names = ["Narnia", "Arendelle", "Naboo"]
    assert direct_flights(planets, names) == (False, 0)


@pytest.fixture
def planets():
    graph = Graph()

    metroville = graph.add_node("Metroville")
    pandora = graph.add_node("Pandora")
    arendelle = graph.add_node("Arendelle")
    new_monstropolis = graph.add_node("New Monstropolis")
    naboo = graph.add_node("Naboo")
    narnia = graph.add_node("Narnia")

    graph.add_edge(pandora, arendelle, 150)
    graph.add_edge(arendelle, pandora, 150)

    graph.add_edge(pandora, metroville, 82)
    graph.add_edge(metroville, pandora, 82)

    graph.add_edge(metroville, arendelle, 99)
    graph.add_edge(arendelle, metroville, 99)

    graph.add_edge(new_monstropolis, arendelle, 42)
    graph.add_edge(arendelle, new_monstropolis, 42)

    graph.add_edge(new_monstropolis, metroville, 105)
    graph.add_edge(metroville, new_monstropolis, 105)

    graph.add_edge(new_monstropolis, naboo, 73)
    graph.add_edge(naboo, new_monstropolis, 73)

    graph.add_edge(metroville, naboo, 26)
    graph.add_edge(naboo, metroville, 26)

    graph.add_edge(metroville, narnia, 37)
    graph.add_edge(narnia, metroville, 37)

    graph.add_edge(narnia, naboo, 250)
    graph.add_edge(naboo, narnia, 250)

    return graph

################
### My tests ###
################

def test_city_itself(planets):
    names = ["Narnia"]
    assert direct_flights(planets, names) == (True, 0)

def test_no_connection(planets):
    names = ["Narnia", "Arendelle"]
    assert direct_flights(planets, names) == (False, 0)

def test_do_connection(planets):
    names = ["Narnia", "Metroville","Arendelle"]
    assert direct_flights(planets, names) == (True, 136)

def test_no_such_city(planets):
    names = ["Narnia", "Seattle"]
    assert direct_flights(planets, names) == (False, 0)
