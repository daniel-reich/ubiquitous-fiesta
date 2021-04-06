
def lucky_seven(lst):
  return any(7-lst[i]-lst[j] in lst[j+1:] for i in range(len(lst)-2) for j in range(i+1,len(lst)-1))

