
def complete_bracelet(lst):
  if len(lst) % 2 != 0: return False
  a = [[lst[j*i:(j+1)*i] for j in range(len(lst) // i)] for i in range(2, len(lst) // 2 + 1) ]
  return any(all(x == lst2_3[0] for x in lst2_3) for lst2_3 in a)

