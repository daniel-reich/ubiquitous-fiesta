
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
​
    def insert(self, data):
        if(self.isEmpty()):
            self.data = data
        elif(data < self.data):
            if(isinstance(self.left, Node)):
                self.left.insert(data)
            else:
                self.left = Node(data)
        elif(data > self.data):
            if(isinstance(self.right, Node)):
                self.right.insert(data)
            else:
                self.right = Node(data)
​
    def PrintTree(self):
        if(self.left == None and self.right == None):
            return [self.data]
        elif(self.left == None):
            return [self.data] + self.right.PrintTree()
        elif(self.right == None):
            return self.left.PrintTree() + [self.data]
        else:
            return self.left.PrintTree() + [self.data] + self.right.PrintTree()
​
    def isEmpty(self):
        return self.data == None

