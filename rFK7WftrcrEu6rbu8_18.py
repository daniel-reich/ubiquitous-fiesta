
# Node class
class Node:
​
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None    
​
# BST Class   
class BST:
​
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
      ans = []
      queue = [self.head]
      while len(queue) > 0:
          cur = queue.pop(0)
          ans.append(cur.data)
          if cur.left != None:
              queue.append(cur.left)
          if cur.right != None:
              queue.append(cur.right)
      return ans

