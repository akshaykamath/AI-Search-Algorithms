__author__ = 'Akshay'

from Node import Node
from Color import Color


class Dfs:
    __adjacency_dict__ = {}
    __visit_time__ = 0
    __searched_list__ = []

    source = None
    destination = None
    distance = 0
    found = False

    def __init__(self, adjacency_dict, source, destination):
        self.__adjacency_dict__ = adjacency_dict  # instance variable unique to each instance
        self.source = source
        self.destination = destination

    def dfs(self, adj_node):
        assert isinstance(adj_node, Node)

        adj_node.color = Color.gray

        for node_tup in adj_node.child_nodes:
            vertex = node_tup[0]
            assert isinstance(vertex, Node)

            if self.found:
                break

            if vertex.color is Color.white:
                vertex.parent_node = adj_node
                vertex.parent_distance = int(node_tup[1])

                if vertex.name.strip().lower() == self.destination:
                    self.found = True

                self.dfs(vertex)

        adj_node.color = Color.black
        if not self.found:
            return

        self.distance += adj_node.parent_distance
        adj_node.finish_time = self.__visit_time__
        self.__searched_list__.append(adj_node)

    def perform_dfs(self):
        for adj_node in self.__adjacency_dict__.itervalues():
            assert isinstance(adj_node, Node)

            if adj_node.name.strip().lower() == self.source and adj_node.color is Color.white:
                self.dfs(adj_node)

    def print_path(self):

        if self.__searched_list__.__len__() < 1:
            print "Path not found."
            return

        for adj_node in self.__searched_list__:
            assert isinstance(adj_node, Node)
            print adj_node.name, " ", adj_node.parent_distance

        print "Total distance : ", self.distance