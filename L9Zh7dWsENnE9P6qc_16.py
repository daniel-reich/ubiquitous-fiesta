
from collections import defaultdict
def josephus(people):
  persons = list(range(people))
  pos = 0
  while len(persons) > 1:
    del persons[(pos+1)%len(persons)]
    pos = (pos+1)%(len(persons)+1)
  return persons[0]+1

