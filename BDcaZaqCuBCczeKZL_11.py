
def arrow(num):
  arr = ['>'*(i+1) for i in range(num)]
  if num%2==0:
    for i in arr[::-1]:
      arr.append(i)
  else:
    for i in arr[::-1][1:]:
      arr.append(i)
  return arr

