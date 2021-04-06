
def simple_numbers(a, b):
  arr = []
  for i in range(a, b+1):
    s = str(i)
    brr = []
    for j in range(len(s)):
      brr.append(int(s[j])**(j+1))
      
    if sum(brr) == i:
        arr.append(i)
  return arr

