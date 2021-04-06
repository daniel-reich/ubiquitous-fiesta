
def standard_deviation(lst):
  mean = sum(lst)/ len(lst)
  mean_square = sum([(abs(i- mean) ** 2) for i in lst]) / len(lst)
  return round(mean_square ** 0.5,2)

