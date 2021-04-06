
def freq_count(lst, el):
  results = [[0,0]]
  investigate = [[0,lst]]
  while investigate:
    current_list = investigate.pop(0)
    for item in current_list[1]:
      if isinstance(item,list):
        depth = current_list[0]+1
        investigate.append([depth,item])
        if depth==len(results):
          results.append([depth,0])
      else:
        if item==el:
          results[current_list[0]][1] += 1
  return results
    
​
print(freq_count([1, [2], 1, [[2]], 1, [[[2]]], 1, [[[[2]]]]], 2))
#[[0, 0], [1, 1], [2, 1], [3, 1], [4, 1]]
print(freq_count([1, 5, 5, [5, [1, 2, 1, 1], 5, 5], 5, [5]], 5))
# [[0, 3], [1, 4], [2, 0]]
print(freq_count([1, 4, 4, [1, 1, [1, 2, 1, 1]]], 1))
#[[0, 1], [1, 2], [2, 3]]

