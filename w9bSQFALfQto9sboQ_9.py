
def gcd(n1, n2):
  print(n1, n2)
  div1 = set()
  for i in range(1, n1 + 1):
    if n1 / i == n1 // i:
      div1.add(i)
  print(div1)
  div2 = set()
  for i in range(1, n2 + 1):
    if n2 / i == n2 // i:
      div2.add(i)
  print(div2)
  divs = div1.intersection(div2)
  return max(divs)

