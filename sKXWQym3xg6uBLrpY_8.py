
def iqr(lst):
  median = lambda n: n[int(len(n)//2)] if len(n)%2 else (n[len(n)//2-1]+n[int(len(n)//2)])/2
  parts = [sorted(lst)[:int(len(lst)//2)],sorted(lst)[int(len(lst)//2)+(len(lst)%2):]]
  return median(parts[1])-median(parts[0])

