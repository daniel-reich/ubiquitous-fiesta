
def closing_in_sum(n):
  s = str(n)
  extra = int(s[len(s)//2]) if len(s)%2==1 else 0
  return sum(int(s[i]+s[-i-1]) for i in range(len(s)//2))+extra

