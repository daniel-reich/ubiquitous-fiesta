
def rev(n):
  n = str(abs(n))
  result = ""
  for i in range(0, len(n)):
    result += n[len(n)-i-1]
  return result

