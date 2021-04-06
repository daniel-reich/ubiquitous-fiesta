
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
​
    def insert(self, data):
        if data == self.data:
            return     
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        if data > self.data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)
​
    def PrintTree(self):
        elements = []
        if self.left:
            elements += self.left.PrintTree()
        elements.append(self.data)
        if self.right:
            elements += self.right.PrintTree()
        return elements

