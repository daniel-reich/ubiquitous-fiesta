
def reverse_odd(txt):
  if(txt == ""):
    return txt
  else:
    ss = list(txt.strip().split(' '))
    ret = ""
    for i in range(0,len(ss)):
      k = list(ss[i].strip())
      if(len(k)%2 == 0):
        ret += ss[i]
      else:
        k = k[::-1]
        for p in k:
          ret += str(p)
      if(i != (len(ss)-1)):
        ret += " "
    return ret

