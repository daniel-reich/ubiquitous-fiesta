
def is_triplet(n1, n2, n3):
  p = sorted([n1,n2,n3])
  return (p[0])**2 + (p[1])**2 == (p[2])**2
​
print(is_triplet(1,9,5))

