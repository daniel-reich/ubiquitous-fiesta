
def fruit_salad(fruits):
  A=[[x[:-((len(x)+1)//2)], x[-((len(x)+1)//2):]] for x in fruits]
  return ''.join(sorted(sum(A,[])))

