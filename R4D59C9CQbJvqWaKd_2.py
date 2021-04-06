
def batting_avg(lst):
  res=sum(lst[i][0] for i in range(len(lst)))/sum(lst[i][1] for i in range(len(lst)))
  return str(round(res,3))[1:]+'0'*(5-len(str(round(res,3))))

