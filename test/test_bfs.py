# write tests for bfs
import pytest
from search.graph import Graph


def test_bfs_traversal():
    """
    BFS traversal test. Creates an instance of your Graph class 
    using the 'tiny_network.adjlist' file and asserts 
    that all nodes are being traversed (ie. returns
    the right number of nodes and in the right order)
    """

    tiny = Graph('/Users/sancheta/Desktop/Classes/Algo/HW2-BFS/data/tiny_network.adjlist')

    fulltraversal = ['Luke Gilbert', '33483487', '31806696', '31626775', '31540829', 
                'Martin Kampmann', 'Neil Risch', 'Nevan Krogan', 
                '32790644', '29700475', '34272374', '32353859', '30944313', 
                'Steven Altschuler', 'Lani Wu', 'Michael Keiser', 'Atul Butte', 
                'Marina Sirota', 'Hani Goodarzi', '32036252', '32042149', 
                '30727954', '33232663', '33765435', '33242416', '31395880', 
                '31486345', 'Michael McManus', 'Charles Chiu', '32025019']
    
    assert tiny.bfs('Luke Gilbert') == fulltraversal #check that it goes in the correct order when traversing
    
    assert len(tiny.bfs('Luke Gilbert')) == len(set(list(tiny.graph.nodes))) #check that we visit each node once in the traversal

    assert tiny.bfs('Luke Gilbert', 'Martin Kampmann') == ['Luke Gilbert', '33483487', 'Martin Kampmann'] #it takes the shortest path between two

def test_bfs():
    """
    Breadth-first search test. Generates an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and asserts that nodes that are connected return 
    a (shortest) path between them.
    
    This include an additional test for nodes that are not connected, ensuring it returns None. 
    """
    
    big = Graph('/Users/sancheta/Desktop/Classes/Algo/HW2-BFS/data/citation_network.adjlist')

    assert big.bfs('Hao Li', 'Katie Pollard') is None #there is no path between Hao Li and Katie Pollard, so it returns None

    assert big.bfs('Atul Butte', 'Katie Pollard') == ['Atul Butte', '33765435', 'Marina Sirota', '21993624', 'Katie Pollard'] #shortest path is connected by Marina Sirota and joint papers


def test_no_endnode():
    """
    Tests BFS search for end node that is not in the graph. Tony Capra is not in the tiny network.
    """

    tiny = Graph('/Users/sancheta/Desktop/Classes/Algo/HW2-BFS/data/tiny_network.adjlist')

    with pytest.raises(ValueError):
        tiny.bfs('Luke Gilbert', 'Tony Capra') #Tony is not found in the graph as an end node, so it raises a value error

def test_no_startnode():
    """
    Tests BFS traversal for start node that is not in the graph. Tony Capra is not in the network.
    """

    tiny = Graph('/Users/sancheta/Desktop/Classes/Algo/HW2-BFS/data/tiny_network.adjlist')

    with pytest.raises(ValueError):
        tiny.bfs('Tony Capra') #Tony is not found in the graph as a start node, so it raises a value error


def test_emptygraph():
    """
    Tests BFS traversal value error for empty file
    """

    empty = Graph('/Users/sancheta/Desktop/Classes/Algo/HW2-BFS/data/empty.adjlist')

    with pytest.raises(ValueError):
        empty.bfs('Tony Capra')



