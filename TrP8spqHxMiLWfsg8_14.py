
class Node:
    tree=[]
​
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        # Hint this line to clear the list for every object
        Node.tree.clear()
​
    def insert(self, val):
        if val >= self.data:
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.insert(val)
        else:
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.insert(val)
​
    def PrintTree(self):
        if self.left is not None:
            self.left.PrintTree()
        Node.tree.append(self.data)
        if self.right is not None:
            self.right.PrintTree()
        return Node.tree

