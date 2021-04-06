
def frac_round(frac, n):
  lst=frac.split('/')
  a='{0:.{b}f}'.format(round(int(lst[0])/int(lst[1]),n),b=n)
  return "{} rounded to {} decimal places is {}".format(frac,str(n),a)

