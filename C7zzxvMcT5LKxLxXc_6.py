
Map = {'a': 16, 'b': 17, 'c': 18, 'x': 3, 'y': 4, 'z': 5, ' ': 5}
for c in range(99, 110):
    Map[chr(c)] = c - 99
for c in range(110, 120):
    Map[chr(c)] = c - 108
for o in range(65, 91):
    c = chr(o)
    Map[c] = Map[c.lower()] + 4
​
def decode(txt):
    ans = [Map.get(c, '?') for c in txt]
    return ans

