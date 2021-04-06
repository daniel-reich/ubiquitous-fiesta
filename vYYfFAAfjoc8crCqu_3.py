
def tree(h):
  try:
    lst = [n for n in range(0,h*2) if n%2!=0]
    w = max(lst)
    return [' '*((w-n)//2)+n*'#'+' '*((w-n)//2) for n in lst]
  except:
    return []

