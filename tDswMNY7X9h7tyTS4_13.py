
def fac(n):
  if n == 0:
    return 1
  else:
    return n * fac(n-1)
​
def arr_pas(n):
    arr_res = []
    for i in range(n+1):
        item = fac(n)/(fac(i)*fac(n-i))
        arr_res.append(int(item))
    return arr_res
  
def pascals_triangle(n):
  arr_res = []
  for i in range(n):
    arr_res += arr_pas(i)
  return arr_res

