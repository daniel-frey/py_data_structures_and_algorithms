import pytest
from .graph import Graph


@pytest.fixture()
def graph_empty():
    g = Graph()
    return g


@pytest.fixture()
def graph_filled():
    g = Graph()
    g.graph = {
        'A': {'B': 10},
        'B': {'A': 5, 'D': 15, 'C': 20},
        'C': {},
        'D': {'A': 5},
        'E': {},
        'F': {}
    }
    return g


@pytest.fixture()
def graph_filled_for_traversal():
    g = Graph()
    g.graph = {
        'A': {'B': 10, 'C': 15},
        'B': {'D': 15, 'E': 5, 'C': 2},
        'C': {'F': 50, 'G': 25},
        'D': {},
        'E': {'C': 5},
        'F': {'E': 10},
        'G': {'F': 20}
    }
    return g


def test_that_graph_exists():
    """Test that the graph class has been imported correctly"""
    assert Graph


def test_graph_add_edge(graph_filled):
    """Test the add method on the graph class"""
    graph_filled.add_edge('C', 'A', 77)
    assert graph_filled.graph == {
        'A': {'B': 10},
        'B': {'A': 5, 'D': 15, 'C': 20},
        'C': {'A': 77},
        'D': {'A': 5},
        'E': {},
        'F': {}
    }


def test_graph_add_vertex(graph_filled):
    """Test the add vertex method on a graph class"""
    graph_filled.add_vert('G')
    assert graph_filled.graph == {
        'A': {'B': 10},
        'B': {'A': 5, 'D': 15, 'C': 20},
        'C': {},
        'D': {'A': 5},
        'E': {},
        'F': {},
        'G': {},
    }


def test_has_vertex(graph_filled):
    """Test for a vertext that exists in the graph"""
    assert graph_filled.has_vert('D')


def test_does_not_have_vertex(graph_filled):
    """Test for a vertex that does not exist in the graph"""
    assert not graph_filled.has_vert('Z')


def test_empty_does_not_have_vertex(graph_empty):
    """Test an empty graph for a vertex that does not exist"""
    assert not graph_empty.has_vert('Z')


def test_neighbor_does_not_exist(graph_filled):
    """Test for a graph that does not have a value"""
    assert graph_filled.get_neighbors('Z') == []


def test_neightbor_exists(graph_filled):
    """Test for a vertex that does have a neighbor"""
    assert graph_filled.get_neighbors('A') == {'B': 10}.keys()


def test_return_correct_length(graph_filled):
    """Test the correct length of a graph"""
    assert len(graph_filled) == 6


def test_return_length_of_empty(graph_empty):
    """Test that an empty graph does return zero"""
    assert len(graph_empty) == 0
