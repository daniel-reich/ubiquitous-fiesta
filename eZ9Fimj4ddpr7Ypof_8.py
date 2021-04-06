
def mumbling(s):
  result = [s[i-1:i] * i for i in range(1,len(s) +1)]
  return "-".join([i.title() for i in result])

