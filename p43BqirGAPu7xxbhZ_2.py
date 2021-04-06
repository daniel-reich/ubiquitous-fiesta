
def diamond(carat):
  lst = []
  for row in range(carat):
    for col in range(carat):
      if row + col == int(carat/2 - 0.1) or row - col == int(carat/2) or col - row == int(carat/2) or row + col == round(carat/2-0.1)-1 + carat:
        lst.append(1)
      else:
        lst.append(0)
  lst = [lst[i:i + carat] for i in range(0, len(lst), carat)]
  if carat % 2 != 0:
    return [lst, 'perfect cut'] 
  else:
    del lst[int(len(lst)/2)]
    return [lst, 'good cut']

