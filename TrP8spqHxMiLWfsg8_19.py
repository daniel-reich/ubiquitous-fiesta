
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
​
    def insert(self, data):
        if self.data < data:
            if self.right == None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        elif self.data > data:
            if self.left == None:
                self.left = Node(data)
            else:
                self.left.insert(data)
​
    def returnList(self):
        treeValues = [self.data]
        if self.left != None:
            treeValues = self.left.returnList() + treeValues
        if self.right != None:
            treeValues = treeValues + self.right.returnList()
        return treeValues
​
    def PrintTree(self):
        return self.returnList()

