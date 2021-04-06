
def is_astonishing(num):
  s_num=str(num)
  lst=[(int(s_num[:i]),int(s_num[i:])) for i in range(1,len(s_num))]
  for a,b in lst:
    if (sum([i for i in range(b,a+1)]) or sum([i for i in range(a,b+1)]))==num:
      return "AB-Astonishing" if a<b else "BA-Astonishing"
  return False

