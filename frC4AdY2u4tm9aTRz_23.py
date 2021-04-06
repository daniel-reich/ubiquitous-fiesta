
def standard_deviation(lst):
  mean=sum(lst)/len(lst)
  sum1=0
  for i in lst:
    sum1=sum1+(i-mean)*(i-mean)
  return round(pow(sum1/len(lst),0.5),2)

