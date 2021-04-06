
def portion_happy(ns):
  return sum(ns[max(0,i-1):i+2].count(ns[i])>1 for i in range(len(ns)))/len(ns)

