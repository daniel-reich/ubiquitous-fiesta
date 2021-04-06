
class Node:
​
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
​
    def insert(self, data):
        nd = self
        while ((data < nd.data and not (nd.left is None))
               or (data > nd.data and not (nd.right is None))):
            if data < nd.data:
                nd = nd.left
            elif data > nd.data:
                nd = nd.right
        if data < nd.data:
            nd.left = Node(data)
        elif data > nd.data:
            nd.right = Node(data)
​
    def PrintTree(self):
        lst_data = []
        lst_node = [self]
        while lst_node:
            new_nodes = []
            for nd in lst_node:
                lst_data.append(nd.data)
                if not (nd.left is None):
                    new_nodes.append(nd.left)
                if not (nd.right is None):
                    new_nodes.append(nd.right)
            lst_node = new_nodes
        return sorted(lst_data)

