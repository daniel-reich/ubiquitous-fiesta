
# Please don't modify the code below the traverse function is in BST class
​
# Node class
​
​
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
# BST Class
​
​
class BST:
    def __init__(self):
        self.head = None
​
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
​
    def traverse(self):
        m = []
        q = []
        q.append(self.head)
        while len(q):
            x = q.pop(0)
            m.append(x.data)
            if x.left:
                q.append(x.left)
            if x.right:
                q.append(x.right)
        return m

