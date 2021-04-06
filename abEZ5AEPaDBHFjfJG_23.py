
def with_a(txt):
  for a in range(1,100):
    lst = txt.split('=')
    for i in range(len(lst)-1):
      if eval(lst[i]) == eval(lst[i+1]):
        return True
  return False
  
def no_a(txt):
  lst = txt.split('=')
  for i in range(len(lst)-1):
    if eval(lst[i]) != eval(lst[i+1]):
      return False
  return True       
​
def formula(txt):
  return with_a(txt) if 'a' in txt else None if not len(txt) else no_a(txt)

