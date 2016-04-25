__author__ = 'Akshay'

from Node import Node
from Color import Color


class Ids:
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

    def iterative_deepening(self, adj_node, depth):
        assert isinstance(adj_node, Node)

        if self.found is True:
            self.__searched_list__.append(adj_node)
            return

        if depth is 0:
            return

        elif depth > 0:
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

                    self.iterative_deepening(vertex, depth - 1)

            if not self.found:
                adj_node.color = Color.white
                return

            adj_node.color = Color.black
            self.__searched_list__.append(adj_node)
        else:
            return None

    def perform_iterative_deepening(self, source_node):
        assert isinstance(source_node, Node)

        count = 0
        while self.found is False:
            self.iterative_deepening(source_node, count)

            count += 1

            if count == 1000000:
                input = raw_input("Depth of 1 million reached, do you still want to continue? y/n, default will be y:")

                if input.strip().lower() is not 'y':
                    break

    def perform_searching(self):
        for adj_node in self.__adjacency_dict__.itervalues():
            assert isinstance(adj_node, Node)

            if adj_node.name.strip().lower() == self.source:
                self.perform_iterative_deepening(adj_node)


    def print_path(self):
        if self.__searched_list__.__len__() < 1:
            print "Path not found."
            return

        for adj_node in self.__searched_list__:
            assert isinstance(adj_node, Node)
            print adj_node.name, " ", adj_node.parent_distance
            self.distance += adj_node.parent_distance

        print "Total distance : ", self.distance
