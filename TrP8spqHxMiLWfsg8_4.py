
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
        if self.data == data:
            return
        if data < self.data:
            # insert in left subtree:
            if self.left == None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            # insert in right subtree:
            if self.right == None:
                self.right = Node(data)
            else:
                self.right.insert(data)
                
    
    def PrintTree(self, root=True, seq=[]):
        if root:
            seq = []
        if self.left != None:
            seq = self.left.PrintTree(False, seq)
        seq.append(self.data)
        if self.right != None:
            seq = self.right.PrintTree(False, seq)
        return seq

