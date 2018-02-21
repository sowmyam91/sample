class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert_node(self, n_value):
        if self.data >= n_value:
            if self.left is None:
                self.left = node(n_value)
            else:
                self.left.insert_node(n_value)
        else:
            if self.right is None:
                self.right = node(n_value)
            else:
                self.right.insert_node(n_value)

    def print_tree(self):

        if self.right:
            self.right.print_tree()
        print(self.data)
        if self.left:
            self.left.print_tree()

    def find_node(self, node_val, parent=None):
        if node_val < self.data:
            if self.left is None:
                return None, None
            return self.left.find_node(node_val, self)
        elif node_val > self.data:
            if self.right is None:
                return None, None
            return self.right.find_node(node_val, self)
        else:
            return self, parent


t = node(4)
t.insert_node(3)
t.insert_node(5)
t.insert_node(2)
t.insert_node(31)
t.print_tree()
