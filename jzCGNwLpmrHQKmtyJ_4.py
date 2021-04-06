
def parityAnalysis(num):
  return not (num-sum(list(map(int,str(num)))))%2

