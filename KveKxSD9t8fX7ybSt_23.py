
import re
def final_countdown(lst):
  lst = re.findall(r'54321|(?<!5)4321|(?<!4)321|(?<!3)21|(?<!2)1',''.join(list(map(lambda x: str(x),lst))))
  y = list(map(lambda x: list(map(lambda y: int(y),x)),lst))
  return [len(lst),y]

