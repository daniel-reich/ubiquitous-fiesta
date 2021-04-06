
def to_list(num):
  return list(int(str(num)[n])for n in range(len(str(num))))
​
​
def to_number(lst):
  return int("".join(str(lst[n]) for n in range(len(lst))))

