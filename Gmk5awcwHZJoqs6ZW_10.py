
import itertools as it
​
class Map(object):
    """docstring for Map"""
    def __init__(self, _map):
        super(Map, self).__init__()
        self.map = _map
        self.dim = len(self.map), len(self.map[0])
        
    def valid_loc(self, loc):
        try:
            self[loc]
        except IndexError:
            return False
​
        return True
​
    def neighbours(self, loc):
        r, c = loc
​
        rng = [-1, 0, 1]
        return set(
            (r + row, c + col) for row, col in it.product(rng, rng)
            if  self.valid_loc((r + row, c + col))
            and (r + row, c + col) != loc
        )
​
    def __getitem__(self, loc):
        row, col = loc
​
        if any([row < 0, col < 0]):
            raise IndexError('location can\'t be less than 0')
​
        return self.map[row][col]
            
    def largest_continent(self):
        visited = set()
        continents = []
​
        dr, dc = self.dim
        for loc in it.product(range(dr), range(dc)):
            if loc in visited: continue
​
            visited.add(loc)
            
            if self[loc] == 0: continue
            
            # Check if any neighbours already in continents
            # If yes, add loc to continent
            # If no,  create new continent
            in_continent = False
            for n in self.neighbours(loc):
                for i in range(len(continents)):
                    if n in continents[i]:
                        continents[i].append(loc)
                        in_continent = True
                        break
​
                if in_continent: break
​
            if not in_continent:
                continents.append([loc])
​
        return max(map(len, continents), default=0)
​
def largest_island(lst):
  return Map(lst).largest_continent()

