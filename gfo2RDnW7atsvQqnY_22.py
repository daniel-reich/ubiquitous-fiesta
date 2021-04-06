
def count_smileys(lst):
  x = 0
  eyes = ":;"
  nose = "-~"
  face = "D)"
  for i in lst:
    if len(i) == 2:
      if i[0] in eyes and i[1] in face:
        x+=1
    elif len(i) == 3:
      if i[0] in eyes and i[1] in nose and i[2] in face:
        x+=1
  return x

