
import numpy as np
import itertools
​
inf = float("inf")
# nan = np.nan
​
​
class Grid():
    def __init__(self, world, width, height):
        self.originalGraph = np.array(world.split(","), dtype=object).reshape(height, width)
        self.graph, self.start, self.goal = self.preprocess(self.originalGraph)
        self.unvisited = set(zip(*np.where(self.graph == inf)))
        self.unvisited.add(self.start)
        self.activelist = set([self.start])
        self.pathLength = self.djkstra(self.start)
​
    @staticmethod
    def preprocess(A):
        start = next(zip(*np.where(A == "m")))
        goal = next(zip(*np.where(A == "h")))
        A[goal] = A[A == "."] = inf
        A[start] = 0
        return A, start, goal
​
    @staticmethod
    def surrounding(A, node):
        ranges = list(list(range(max(n - 1, 0), min(n + 2, r))) for n, r in zip(node, A.shape))
        return set(itertools.product(*ranges))
​
    def djkstra(self, activenode):
        if activenode != self.goal:
            self.unvisited.remove(activenode)
            look = set()
            for x in self.surrounding(self.graph, activenode):
                if x != "t" and x in self.unvisited:
                    look.add(x)
                    self.activelist.add(x)
            self.activelist.remove(activenode)
            if not self.activelist:
                return -1
            else:
                for x in look:
                    self.graph[x] = min(self.graph[x], self.graph[activenode] + 1)
                activenode = min((x for x in self.activelist), key=lambda x: self.graph[x])
                return self.djkstra(activenode)
​
        else:
            return self.graph[self.goal]
​
def get_path_length(world, width, height):
    test = Grid(world, width, height)
    return test.pathLength

