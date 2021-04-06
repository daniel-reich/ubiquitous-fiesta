
def count_layers(rug):
  lyr = 0
  middle_layer = rug[len(rug)//2]
  fchar = ""
  for c in middle_layer[:len(middle_layer)//2 + 1]:
    if c != fchar:
      fchar = c
      lyr += 1
  return lyr

