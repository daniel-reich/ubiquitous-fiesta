
def isbn13(txt):
  lst = [int(i) if i.isdigit() else 10 for i in txt]
  
  if val_13(lst):
    return 'Valid'
  elif val_10(lst):
    lst = [9,7,8] + lst[:-1]
    for i in range(10):
      temp = lst + [i]
      if val_13(temp):
        return ''.join(str(i) for i in temp)  
  return 'Invalid'
​
def val_13(lst):
  return len(lst) == 13 and not sum(lst[i] if not i%2 else lst[i]*3 for i in range(13))%10
​
def val_10(lst):
  return len(lst) == 10 and not sum(lst[i-1]*i for i in range(10,0,-1))%11

