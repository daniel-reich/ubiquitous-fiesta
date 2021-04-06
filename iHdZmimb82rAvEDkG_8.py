
def bitwise_index(lst):
  largest = [float("-inf")] #infinitely small lower bound
  for i in range(len(lst)):
    if lst[i] / 2 == lst[i] // 2 and lst[i] > largest[0]:
      largest = [lst[i], i]
  return "No even integer found!" if len(largest) == 1 else {"@" + ("even" if largest[1] / 2 == largest[1] // 2 else "odd") + " index %s" % largest[1]: largest[0]}

