
def closing_in_sum(n):
  txt = str(n)
  mid = len(txt)//2
  res = sum(int(txt[i] + txt[-i-1]) for i in range(mid))
  return (res + int(txt[mid])) if len(txt)%2 else res

