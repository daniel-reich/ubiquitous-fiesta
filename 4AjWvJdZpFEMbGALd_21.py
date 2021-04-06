
def who_goes_free(n, k):
  prisoners = list(range(n))
  cuenta = 1
​
  while len(prisoners) > 1:
​
    for i in range(len(prisoners)):
​
      if cuenta % k == 0:
        prisoners[i] = "x"
      cuenta += 1
​
      if cuenta > k:
        cuenta = 1
    prisoners = [x for x in prisoners if x != "x"]
​
  return prisoners[0]

