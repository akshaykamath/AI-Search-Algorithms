__author__ = 'leeladhar'

from Node import Node
from Color import Color
from pythonds.basic import Queue


class Bfs:
    __adjacency_dict__ = {}
    __searched_list__ = []
    total_distance = 0
    source = None
    destination = None
    found = False

    def __init__(self, adjacency_dict, source, destination):
        self.__adjacency_dict__ = adjacency_dict  # instance variable unique to each instance
        self.source = source
        self.destination = destination

    def bfs(self, adj_node):
        adj_node.color = Color.gray
        adj_node.parent_node = None
        adj_node.parent_distance = 0

        node_queue = Queue()
        node_queue.enqueue(adj_node)

        while node_queue.size() > 0:
            adj_node = node_queue.dequeue()

            if self.found:
                break

            for node_tup in adj_node.child_nodes:
                vertex = node_tup[0]
                assert isinstance(vertex, Node)

                if vertex.color is Color.white:
                    vertex.color = Color.gray
                    vertex.parent_distance = int(node_tup[1])
                    vertex.parent_node = adj_node
                    node_queue.enqueue(vertex)

                if vertex.name.strip().lower() == self.destination:
                    self.found = True
                    self.__searched_list__.append(vertex)
                    break

            adj_node.color = Color.black

    def perform_bfs(self):
        for adj_node in self.__adjacency_dict__.itervalues():
            assert isinstance(adj_node, Node)

            if adj_node.name.strip().lower() == self.source and adj_node.color is Color.white:
                self.bfs(adj_node)

    def print_path(self):
        if self.__searched_list__.__len__() < 1:
            print "Path not found."
            return

        destination_node = self.__searched_list__[0]
        total_distance = 0

        while destination_node is not None:
            assert isinstance(destination_node, Node)

            print destination_node.name, " ", destination_node.parent_distance
            total_distance += destination_node.parent_distance
            destination_node = destination_node.parent_node

        print "Total Distance: ",total_distance
