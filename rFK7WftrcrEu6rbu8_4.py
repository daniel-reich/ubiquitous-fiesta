
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
    sol = []
    queue = []
    print(self.head)
    if (self.head is not None):
        node = self.head
        if (node is not None):
            sol.append(node.data)
        queue.append(node.left)
        queue.append(node.right)
        while queue != []:
            if (queue[0] is not None):
                sol.append(queue[0].data)
                queue.append(queue[0].left)
                queue.append(queue[0].right)
                queue.pop(0)
            else:
                queue.pop(0)
        return sol
    else:
        return []

