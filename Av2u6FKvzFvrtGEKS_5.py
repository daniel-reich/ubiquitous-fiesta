
class Node(object):
  def __init__(self, data): self.data,self.next = data,None
​
class LinkedList(object):
  def __init__(self): self.head,self.tail = None,None
  
  def insert(self, data):
    new_node = Node(data)
    if not self.head: self.head = self.tail = new_node
    else: self.tail.next = new_node; self.tail = new_node
  
  def traverse(self):
    if not self.head: return []
    temp,result = self.head,[]
    while temp!=None: result.append(temp.data); temp = temp.next
    return result
    
  def reverse(self):
    x,self.head,self.tail = self.traverse()[::-1],None,None
    for i in x: self.insert(i)

