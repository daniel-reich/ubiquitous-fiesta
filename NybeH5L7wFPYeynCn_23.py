
def three_letter_collection(x):
  arr = []
  for i in range(len(x)-2):
    arr.append(x[i]+x[i+1]+x[i+2])
​
  return sorted(arr) if len(x) > 2 else []

