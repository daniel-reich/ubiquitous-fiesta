
#Do not touch this starter code but implement the reverse function at the
#end of the LinkedList class
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
​
    def reverse(self):
        # enter code here you don't have to return anything
        l=self.traverse()
        self.__init__()
        for i in range(len(l)-1,-1,-1):
            self.insert(l[i])
        #
        # print(self.traverse())
        # print(self.tail.data)
        # Just take care of head and tail

