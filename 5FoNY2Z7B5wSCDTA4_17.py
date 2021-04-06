
from itertools import count
def happy_year(year):
  for i in count(year + 1):
    if len(set(str(i))) == len(str(i)):
      return i

