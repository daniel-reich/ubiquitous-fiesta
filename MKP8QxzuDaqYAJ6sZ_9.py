
def is_correct_aliases(names, aliases):
  check=0
  y=0
  for x in aliases:
    fake=x.split(" ")
    if names[y][0]!=fake[0][0]:
      check=1
    if names[y][0]!=fake[1][0]:
      check=1
    y+=1
  return not check

