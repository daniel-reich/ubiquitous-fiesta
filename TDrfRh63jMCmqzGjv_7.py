
from collections import Counter
def is_anti_list(lst1, lst2):
  C = Counter(lst1 + lst2);
  return all(1 if a != b else 0 for a,b in zip(lst1,lst2)) and len(C)==2;

