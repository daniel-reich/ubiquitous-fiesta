
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
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
        sol = []
        queue = [self.head]
        while len(queue):
            item = queue.pop(0)
            sol.append(item.data)
            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)
        return sol

