
def largest_island(lst):
  sizes = []
  for i in range(len(lst)):
    for j in range(len(lst[0])):
      if lst[i][j]==1:
        sizes.append(sum([lst[k][l] if abs(k-i)<=1 and abs(l-j)<=1 else 0 for k in range(len(lst)) for l in range(len(lst[0]))]))
  return max(sizes)

