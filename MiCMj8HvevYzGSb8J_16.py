
def fibo_word(n):
  if n < 3:
    return "invalid"
  else:
    seq = ""
    arr = ['b','a']
    for i in range(n-2):
      arr.append(arr[i+1] + arr[i])
  for i in range(len(arr)-1):
    seq += "{}, ".format(arr[i])
  return seq+arr[n-1]

