
def how_bad(n):
  n = bin(n)[2:]
  lst = []
  if n.count("1") % 2 == 0:
    lst.append("Evil")
  else:
    lst.append("Odious")
  primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
            43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
  if int(n.count("1")) in primes:
    lst.append("Pernicious")
  return lst

