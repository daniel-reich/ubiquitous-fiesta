
def adjacent_product(lst):
  count = 0
  emplst= []
  for num in lst:
          while count+1 < len(lst):
              emplst.append((lst[count]*lst[count+1]))
              count += 1
          else:
              break
  return max(emplst)

