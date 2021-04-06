
def min_miss_pos(lst):
   for i in range(1, 2<<64):  # huge range instead of "while" or itertools.count
      if i not in lst:
         return i

