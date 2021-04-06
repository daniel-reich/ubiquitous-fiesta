
def even_odd_string(s):
  return "".join([s[i] for i in range(0,len(s),2)])+" "+"".join([s[i] for i in range(1,len(s),2)])

