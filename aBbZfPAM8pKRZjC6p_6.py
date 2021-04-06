
def fruit_salad(fruits):
  result = []
  for word in fruits:
    mid_index = len(word)//2
    result.append(word[:mid_index])
    result.append(word[mid_index:])
  return "".join(sorted(result))

