
def add_it_up(lst):
  d = {int:0,float:0,list:1,tuple:2}
  return sum(lst,[0,[],()][d[type(lst[0])]])

