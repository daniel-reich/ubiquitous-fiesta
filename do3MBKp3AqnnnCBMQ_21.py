
import random
def numbers():
  result = []
  while len(result) < 5:
    x = random.randint(1,5)
    if str(x) not in result:
      result.append(str(x))
  return int("".join(result))

