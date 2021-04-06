
def show_the_love(lst):
  res = [x*0.75 for x in lst]
  res[res.index(min(res))]+= sum(lst)-sum(res)  
  return res

