
# Node class
class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None    
# BST Class   
class BST:
  def __init__(self):
    self.head = None
  def insert(self, data):
    new_node = Node(data)
    if self.head == None:
      self.head = new_node
    else:
      current = self.head
      while True:
        if data > current.data and current.right:
          current = current.right
        elif data < current.data and current.left:
          current = current.left
        elif data > current.data:
          current.right = new_node
          break
        else:
          current.left = new_node
          break
    return self.head
    
  def traverse(self, s = None):
    s = self.head
    traversal, queue = [], []
    queue.append(s)
    while queue:
      s = queue.pop(0)
      traversal.append(s)
      if s.left and s.left not in traversal: 
        queue.append(s.left)
      if s.right and s.right not in traversal:
        queue.append(s.right)
    return [node.data for node in traversal]

