
def first_and_last(s):
  str1 = "".join(sorted(s))
  str2 = "".join(sorted(s,reverse=True))
  list= [str1,str2]
  return list

