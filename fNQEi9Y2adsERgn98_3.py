
def perimeter(lst):
  return round(sum([((lst[i][0]-lst[i-1][0])**2 + (lst[i][1]-lst[i-1][1])**2)**0.5 for i in range(len(lst))]),2)

