
def arrow(num):
  if num%2:
    A=[i*'>' for i in range(1, num+1)]
    return A+A[:num-1][::-1]
  else:
    A=[i*'>' for i in range(1, num+1)]
    return A+A[:num][::-1]

