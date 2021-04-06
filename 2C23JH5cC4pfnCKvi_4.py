
from collections import Counter
def check_flush(table, hand):
  t = [x.split("_")[1] for x in table]
  h = [x.split("_")[1] for x in hand]
  c = Counter(t)+Counter(h)
  return any(filter(lambda x: x>4,c.values()))
    
​
print(check_flush(["A_S", "J_H", "7_D", "8_D", "10_D"], ["J_D", "3_D"]))

