
def major_sum(lst):
  positive=sum([i for i in lst if i>0])
  negative=sum([i for i in lst if i<0])
  zero=len([i for i in lst if i==0])
  large=max(positive,abs(negative),zero)
  if large==abs(negative):
    return negative
  else:
    return large

