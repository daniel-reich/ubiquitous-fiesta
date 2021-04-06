
class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None
class BST:
  def __init__(self):
    self.head = None
  def insert(self,data):
    node = Node(data)
    if not self.head:
      self.head = node
    else:
      current = self.head
      while True:
        if data < current.data:
          if current.left:
            current = current.left
          else:
            current.left = node
            break
        elif current.right:
          current = current.right
        else:
          current.right = node
          break
  def traverse(self):
    path = []
    queue = [self.head]
    while queue:
      current = queue[0]
      path.append(current)
      if current.left:
        queue.append(current.left)
      if current.right:
        queue.append(current.right)
      queue.pop(0)
    return list(map(lambda x: x.data,path))

