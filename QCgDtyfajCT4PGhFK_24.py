
def prime_factorization(number):
  p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
  lst = []
  i = 0
  while number > 1:
    t = number / p[i]
    if t.is_integer():
      lst.append(p[i])
      number = t
    else:
      i+=1
  return lst

