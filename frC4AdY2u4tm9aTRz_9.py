
def standard_deviation(lst):
 return round(sum((sum(lst)/len(lst) - x)**2/len(lst) for x in lst) ** .5,2)

