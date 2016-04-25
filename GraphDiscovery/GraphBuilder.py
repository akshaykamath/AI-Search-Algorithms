__author__ = 'Akshay'

from Node import Node


class GraphBuilder:
    def __init__(self):
        pass

    @staticmethod
    def print_adj_list(list):
        for node in list.itervalues():
            print "---", node.name, "----"
            for c_node in node.child_nodes:
                print c_node[0].name
                print c_node[1]

            print "-------"

    @staticmethod
    def generate_adjacency_list(file_path):
        adjacency_dictionary = {}
        f = open(file_path, 'r')

        for line in f:
            split = line.replace('\n', '').split(' ')
            node1 = None
            node2 = None

            # Get the first node.
            if split[0] not in adjacency_dictionary.keys():
                node1 = Node(split[0])
                adjacency_dictionary[split[0]] = node1
            else:
                node1 = adjacency_dictionary[split[0]]

            # Get the second node.
            if split[1] not in adjacency_dictionary.keys():
                node2 = Node(split[1])
                adjacency_dictionary[split[1]] = node2
            else:
                node2 = adjacency_dictionary[split[1]]

            if not node1.has_child(node2):
                node1.add_child(node2, split[2])

            if not node2.has_child(node1):
                node2.add_child(node1, split[2])

        return adjacency_dictionary
