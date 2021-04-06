
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
​
​
class BST:
    def __init__(self):
        self.head = None
​
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while True:
                if data > current.data and current.right:
                    current = current.right
                elif data < current.data and current.left:
                    current = current.left
                elif data > current.data:
                    current.right = new_node
                    break
                else:
                    current.left = new_node
                    break
        return self.head
​
    def traverse(self):
        lst_data = []
        level_nods = [self.head]
        while level_nods:
            next_level = []
            for node in level_nods:
                lst_data.append(node.data)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level_nods = next_level
        return lst_data

