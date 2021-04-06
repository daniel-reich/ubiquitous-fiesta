
def count_smileys(lst):
  eyes = [':', ';']
  nose = ['-', '~']
  mouth = [')', 'D']
  count = 0
  for el in lst:
    if len(el) == 2:
      count += 1 if el[0] in eyes and el[1] in mouth else 0
    elif len(el) == 3:
      count += 1 if el[0] in eyes and el[1] in nose and el[2] in mouth else 0
  return count

