
def decode(txt):
  lst = [list(int(y) for y in " ".join(str(ord(i))).split(" ")) for i in txt]
  print(lst)
  lst2 = [sum(i) for i in lst]
  print(lst2)
  return lst2

