
def babbage(n):
  k = len(str(n))
  m = 10**k
  i = 1
  while True:
    if i**2%m == n:
      if n == 269696:
        if i==99736:
          return "Babbage was correct!"
        else:
          return "Babbage was incorrect!"
      return i
    i+=1

