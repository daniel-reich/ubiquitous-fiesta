
def closing_in_sum(n):
  t=len(str(n))//2 +1*(len(str(n))%2==0)
  s=str(n)[:t]+'0'*(len(str(n))%2)+str(n)[t:]
  A=[int(x[0]+x[1]) for x in zip(s[:len(s)//2], s[len(s)//2:][::-1])]
  return sum(A)

