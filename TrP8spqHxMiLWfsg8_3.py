
class Node:
    tree=[]
# crate node for number every nood have left childe and right chile and data
    def __init__(self, data):
​
        self.left = None
        self.right = None
        self.data = data
        Node.tree.clear()
​
    def insert(self, data):
# Compare the new value with the parent node
​
        if self.data:
            # check for the new value if it bigger than the root if it true then check if the root have a left chiled
            # if not have make this data a new node as aleft node for the root and this node have a left and right
            # if the root already have aleft so it recall the func insert but this time to left node to cheack agine
            # if the new inert data is smaller than that nood or not and the same for the right
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
​
# Print the tree
    def PrintTree(self):
        # cheak the object left childe if it has left  child recall the func to cheak again if it have left etc...
        # if it not have  it print the data of that node
        if self.left:
            self.left.PrintTree()
        Node.tree.append(self.data)
        if self.right:
            self.right.PrintTree()
        return Node.tree

