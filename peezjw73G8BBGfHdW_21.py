
def arithmetic_operation(n):
  a = n.replace('//','/').split(' ')
  if a[1] == '+':
    return int(a[0]) + int(a[2])
  elif a[1] == '-':
    return int(a[0]) - int(a[2])
  elif a[1] == '*':
    return int(a[0]) * int(a[2])
  else:
    try:
      return int(a[0]) / int(a[2])
    except:
      return -1

