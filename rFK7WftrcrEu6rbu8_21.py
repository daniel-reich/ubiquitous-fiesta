
# Please don't modify the code below the traverse function is in BST class
​
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
  
  def traverse(self):
    obj_lst = [self.head]
    result = []
    for i in range(50):
      try:
        if obj_lst[i].left not in obj_lst:
          obj_lst.append(obj_lst[i].left)
        if obj_lst[i].right not in obj_lst:
          obj_lst.append(obj_lst[i].right)
      except (AttributeError, IndexError):
        continue
    for j in obj_lst:
      try:
        result.append(j.data)
      except AttributeError:
        continue
    return result

