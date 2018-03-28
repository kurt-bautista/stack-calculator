class Node(object):
    """Node object for linked-list implementation"""

    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class Stack(object):
    """Object-oriented stack impelementation"""

    def __init__(self):
        """Creates a node with null values as end of stack"""
        self.linked_list = Node(None, None)

    def push(self, item):
        """Pushes item to top of stack"""
        node = Node(item, self.linked_list)
        self.linked_list = node

    def pop(self):
        """Returns data at the top of stack"""
        node = self.linked_list
        # Return False if stack is empty
        if node.data is None and node.next_node is None:
            return False
        self.linked_list = self.linked_list.next_node
        return node.data
