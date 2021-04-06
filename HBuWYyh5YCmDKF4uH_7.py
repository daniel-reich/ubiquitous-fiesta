
def almost_sorted(lst):
  lst=[i[1]>i[0] for i in zip(lst,lst[1:])]
  return lst.count(True)==1 or lst.count(False)==1

