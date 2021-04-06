
# Do not touch this starter code but implement the reverse function at the 
# end of the LinkedList class
class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None
​
​
class LinkedList(object):
  def __init__(self):
    self.head = None
    self.tail = None
​
  def insert(self, data):
    new_node = Node(data)
​
    if self.head == None:
      self.head = self.tail = new_node
​
    else:
      self.tail.next = new_node
      self.tail = new_node
​
​
  def traverse(self):
​
    if self.head == None:
      return []
​
    temp = self.head
    result = []
    while temp!=None:
      result.append(temp.data)
      temp = temp.next
​
    return result
    
  def reverse(self):
    # enter code here you don't have to return anything 
    # Just take care of head and tail
    aux = self.head
    self.head = self.tail
    self.tail = aux
    pseudoHead = self.tail
    while (self.tail.next != None):   
      aux = self.tail.next
      self.tail.next = self.tail.next.next
      aux.next = pseudoHead
      pseudoHead = aux
      aux = self.tail.next

