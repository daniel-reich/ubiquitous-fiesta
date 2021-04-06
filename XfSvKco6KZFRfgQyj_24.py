
def find_a_seat(n, lst):
  i = [x for x in range(len(lst)) if lst[x] <= (n/len(lst))/2]
  print(i)
  return i[0] if len(i) != 0 else -1

