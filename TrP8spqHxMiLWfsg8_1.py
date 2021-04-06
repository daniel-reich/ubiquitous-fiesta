
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
        if self.right:
          self.right.insert(data)
        else:
          self.right = Node(data)
      else:
        if self.left:
          self.left.insert(data)
        else:
          self.left = Node(data)
    
  def PrintTree(self):
    def rec_vis(node):
        if not node:
          return []
        return rec_vis(node.left) + [node.data] + rec_vis(node.right)
    return rec_vis(self)

