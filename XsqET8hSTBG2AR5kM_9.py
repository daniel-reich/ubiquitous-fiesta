
def dist(c1, c2):
  return abs(ord(c1) - ord(c2))
​
def letter_distance(s1, s2):
  if len(s1) < len(s2):
    s1,s2 = s2,s1
  return sum(dist(s1[i], s2[i]) for i in range(len(s2))) + len(s1) - len(s2)

