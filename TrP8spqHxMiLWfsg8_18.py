
class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data
​
  def insert(self, data):
    if data == self.data:
      return
    elif data < self.data:
      if self.left:
        self.left.insert(data)
      else:
        self.left = Node(data)
    else:
      if self.right:
        self.right.insert(data)
      else:
        self.right = Node(data)
​
  def PrintTree(self):
    p_data = self.left.PrintTree() if self.left else []
    p_data.append(self.data)
    p_data.extend(self.right.PrintTree() if self.right else [])
    return p_data

