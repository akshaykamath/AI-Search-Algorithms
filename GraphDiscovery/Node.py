__author__ = 'Akshay'

from Color import Color


class Node:
    color = None
    initial_time = 0
    finish_time = 0
    name = None
    child_nodes = None
    parent_node = None

    def __init__(self, nm):
        self.name = nm
        self.parent_distance = 0
        self.child_nodes = []
        self.color = Color.white

    def add_child(self, node=None, weight=None):
        self.child_nodes.append((node, weight))

    def has_child(self, node=None):
        return node in self.child_nodes
