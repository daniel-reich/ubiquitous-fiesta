
def validate_swaps(lst, txt):
  arr = [sum(1 for x,y in zip(word, txt) if x!=y) if len(word) == len(txt) else 5 for word in lst]
  return [True if x == 2 else False for x in arr ]

