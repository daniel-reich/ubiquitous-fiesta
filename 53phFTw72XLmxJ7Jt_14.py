
def marathon_distance(d):
  return True if sum([i if i>0 else i-2*i for i in d]) == 25 else False

