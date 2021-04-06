
def calls(fn, *a):
  try: c = a[0]
  except: c = 0
  if callable(fn):
    c += 1
    return calls(fn(), c)
  else: return c + 1
  
def func_sort(lst): return sorted(lst, key=calls)

