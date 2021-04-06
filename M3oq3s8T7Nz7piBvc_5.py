
def even_odd_string(txt):
  lst1 = "".join([x for y,x in enumerate(txt) if y%2==0])
  lst2 = "".join([x for y,x in enumerate(txt) if y%2==1])
  return "{} {}".format(lst1,lst2)

