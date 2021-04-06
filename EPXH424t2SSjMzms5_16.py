
def remix(txt, lst):
  result = [None]*len(txt)
  for character, position in zip(txt, lst):
    result[position] = character
  return ''.join(result)

