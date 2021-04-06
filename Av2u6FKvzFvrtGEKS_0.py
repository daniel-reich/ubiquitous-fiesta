
class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None
​
class LinkedList(object):
  def __init__(self):
    self.head = None
    self.tail = None
​
  def insert(self, data):
    new_node = Node(data)
    if self.head == None:
      self.head = self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
​
  def traverse(self):
    if self.head == None:
      return []
    temp = self.head
    result = []
    while temp!=None:
      result.append(temp.data)
      temp = temp.next
    return result
    
  def reverse(self):
    prev = None
    curr = self.head
    self.tail = curr
    while curr != None:
      next = curr.next
      curr.next = prev
      prev = curr
      curr = next
    self.head = prev

