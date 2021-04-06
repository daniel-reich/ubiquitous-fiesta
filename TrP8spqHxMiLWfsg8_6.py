
class Node:
    tree=[]
​
    def __init__(self, data):
​
        self.left = None
        self.right = None
        self.data = data
        # Hint this line to clear the list for every object
        Node.tree.clear()
​
    def insert(self, data):
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                node = Node(data)
                self.left = node
        else:  # greater in the examples - all values unique
            if self.right:
                self.right.insert(data)
            else:
                node = Node(data)
                self.right = node
    
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        Node.tree.append(self.data)
        if self.right:
            self.right.PrintTree()
​
        return Node.tree

