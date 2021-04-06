
def count_smileys(lst):
  import re
  sum = 0
  for face in lst:
      if re.match(r'[:;][-~]?[)D]', face):
        sum +=1
  return sum

