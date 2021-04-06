
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
        
        if data > self.data:
            if self.right == None:
                self.right = Node(data)
            else:
                self.right.insert(data)
​
        elif data < self.data:
            if self.left == None:
                self.left = Node(data)
            else:
                self.left.insert(data)
​
        
    def PrintTree(self):
        if self.left != None:
            self.left.PrintTree()
        
        Node.tree.append(self.data)
​
        if self.right != None:
            self.right.PrintTree()
​
        return Node.tree

