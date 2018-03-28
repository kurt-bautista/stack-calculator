class Node(object):
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class Stack(object):
    def __init__(self):
        self.linked_list = Node(None, None)

    def push(self, item):
        node = Node(item, self.linked_list)
        self.linked_list = node

    def pop(self):
        node = self.linked_list
        if node.data is None and node.next_node is None:
            return False
        self.linked_list = self.linked_list.next_node
        return node.data
