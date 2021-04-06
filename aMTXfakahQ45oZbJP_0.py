
def complete_bracelet(lst):
  possible = [[tuple(lst[i:i+j]) for i in range(0,len(lst),j)] for j in range(2,(len(lst)//2)+1) if len(lst)%j == 0]
  return any(len(set(item)) == 1 for item in possible)

