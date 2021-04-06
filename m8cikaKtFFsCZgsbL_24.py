
class State:
    def __init__(self, c = [], a = [], h = []):
        self.c = c
        self.a = a
        self.h = h
​
    def __hash__(self):
        h = 0
        for x in range(0, len(self.c)):
            h += hash(self.c[x])
        for x in range(0, len(self.a)):
            h += hash(self.a[x])
        return h
​
    def __eq__(self, other):
        return self.c == other.c and self.a == other.a
​
    def copy(self):
        return State(self.c.copy(), self.a.copy(), self.h.copy())
​
    def __lt__(self, other):
        return len(self.h) < len(other.h)
​
def waterjug(start, goal, printHistory = False):
    amounts = [0, 0, start[2]]
    queue = []
    queue.append(State(start.copy(), amounts.copy()))
    prev = set()
    while len(queue) > 0:
        n = queue.pop()
        if n.a == goal:
            if printHistory:
                print("start:")
                for x in range(0, len(start)):
                    if x != len(start) - 1:
                        print(" 0/{0}".format(start[x]))
                    else:
                        print(" {0}/{0}".format(start[x]))
                for i in range(0, len(n.h)):
                    print(n.h[i])
            return len(n.h)
        for i in range(0, len(n.a)):
            # fill
#            if n.a[i] != n.c[i]:
#                c = n.copy()
#                c.a[i] = c.c[i]
#                if not c in prev:
#                    s = "fill {0}".format(i)
#                    for x in range(0, len(n.a)):
#                        s += " {0}/{1}".format(c.a[x], c.c[x])
#                    c.h.append(s)
#                    queue.append(c)
#                    queue.sort(reverse=True)
#                    prev.add(c.copy())
            # empty
            if n.a[i] > 0:
                c = n.copy()
                c.a[i] = 0
                if not c in prev:
                    s = "empty {0}".format(i)
                    for x in range(0, len(n.a)):
                        s += " {0}/{1}".format(c.a[x], c.c[x])
                    c.h.append(s)
                    queue.append(c)
                    queue.sort(reverse=True)
                    prev.add(c.copy())
            # pour from one to another
            for j in range(0, len(n.a)):
                if i != j:
                    c = n.copy()
                    if c.a[i] + c.a[j] > c.c[j]:
                        c.a[i] -= c.c[j] - c.a[j]
                        c.a[j] = c.c[j]
                    else:
                        c.a[j] += c.a[i]
                        c.a[i] = 0
                    if not c in prev:
                        s = "pour from {0} to {1}".format(i, j)
                        for x in range(0, len(n.a)):
                            s += " {0}/{1}".format(c.a[x], c.c[x])
                        c.h.append(s)
                        queue.append(c)
                        queue.sort(reverse=True)
                        prev.add(c.copy())
    return "No solution."

