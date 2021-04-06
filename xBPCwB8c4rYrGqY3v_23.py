
def missing(lst):
  mi, ma = min(lst), max(lst)
  for i in range(len(lst)):
    if lst[i] + lst[-i-1] != mi + ma:
      if mi+ma - lst[-i-1] in lst:
        return ma+mi - lst[i]
      else:
        return ma+mi - lst[-i-1]

