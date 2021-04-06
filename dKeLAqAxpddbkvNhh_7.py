
def group_seats(lst, n):
  return sum([x for x in [[1 for j in range(len(i)) if i[j:j+n] == "0"*n] for i in ["".join([str(x) for x in lst[y]]) for y in range(len(lst))]] for x in x])

