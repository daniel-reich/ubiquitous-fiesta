
def ohms_law(v, r, i):
  ls = [0 if x==None else x for x in (v, r, i)]
  if ls.count(0) == 1:
    lst = [x for x in ls if x>0]
    l = ["*", "/", "/"]
    return round(eval("{}{}{}".format(lst[0],l[ls.index(0)],lst[1])), 2)
  else:
    return "Invalid"

