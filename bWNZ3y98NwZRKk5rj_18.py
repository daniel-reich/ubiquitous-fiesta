
def block_player(a, b):
  c = [[0, 1, 2], [0, 3, 6], [1, 4, 7],
       [3, 4, 5], [2, 5, 8], [0, 4, 8],
       [6, 7, 8], [2, 4, 6]]
  for i in c:
      if a in i  and b in i:
          return [j for j in i if j not in [a, b]][0]

