
# Please don't modify the code below the traverse function is in BST class
​
# Node class
class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
​
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
  
  def traverse(self):
    # Complete the code here
    if self.head is None:
      return []
    to_visit = [self.head]
    output = []
    while(to_visit):
      node = to_visit.pop(0)
      output.append(node.data)
      if node.left:
        to_visit.append(node.left)
      if node.right:
        to_visit.append(node.right)
    return output

