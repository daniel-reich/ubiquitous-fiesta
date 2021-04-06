
def is_astonishing(num):
  arr = []
  s = str(num)
  for i in range(int((len(s))/2),int((len(s))/2)+2):
    a = int(s[:i])
    b = int(s[i:])
    if a < b:
      brr = sum(list(range(a,b+1)))
      if brr == num:
        return "AB-Astonishing"
    else : 
      brr = sum(list(range(b,a+1)))
      if brr == num:
        return "BA-Astonishing" 
  return False

