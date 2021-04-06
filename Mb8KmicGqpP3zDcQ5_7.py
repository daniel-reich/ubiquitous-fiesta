
class Node:
​
    def __init__(self, value):
        self.value = value
        self.next = None
​
​
class CircularLinkedList:
​
    def __init__(self):
        self.head = None
    
    def __str__(self):
        arr = []
​
        current = self.head
        
        if self.head:
            while True:
                if current.next == self.head:
                    arr.append(current.value)
                    break
                arr.append(current.value)
                current = current.next
                
​
        return ' -> '.join(map(str, arr))
​
​
​
    
    def push(self, value):
        node = Node(value)
        
        if not self.head:
            self.head = node
            self.head.next = self.head
            return
        
        current = self.head
​
        while current.next != self.head:
            current = current.next
        # print(current.value, node.value)
        node.next = self.head        
        current.next = node
​
        
    
    def push_array(self, array):
        for x in array:
            self.push(x)
​
​
​
def josephus(n, k):
    a = CircularLinkedList()
    a.push_array(range(1,n+1))
​
    killer = a.head
    prev = a.head
​
    if not n:
        return False
    
    while killer.next != killer:
​
        count = 1
        while count != k:
            prev = killer
            killer = killer.next
            count += 1
        
        prev.next = killer.next
        killer = prev.next
    
    return killer.value if killer.value != 1 else n

