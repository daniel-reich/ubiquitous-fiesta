
class Node:
    tree=[]
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right = None
​
    def insert(self, data):
        if self.data > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left=Node(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right=Node(data)
    
    def PrintTree(self):
      Node.tree.clear()
      self.__search()
      return Node.tree
  
    def __search(self):
        if self.left or self.right:
            if self.left:
                left=self.left.__search()
                if left:
                    Node.tree.append(left.data)
            Node.tree.append(self.data)
            if self.right:
                right=self.right.__search()
                if right:
                    Node.tree.append(right.data)
        else:
            return self

