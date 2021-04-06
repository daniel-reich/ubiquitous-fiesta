
def triangle(perimeter,area):
  solutions = []
  for s1 in range(1,perimeter):
    for s2 in range(1,perimeter-s1+1):
      s3 = perimeter - s1 - s2
      if s1+s2+s3 == perimeter:
        if round(16*(area**2)) == (2*(s1**2)*(s2**2))+(2*(s1**2)*(s3**2))+(2*(s2**2)*(s3**2))-s1**4-s2**4-s3**4:
          if sorted([s1,s2,s3]) not in solutions:
            solutions.append(sorted([s1,s2,s3]))
  return solutions

