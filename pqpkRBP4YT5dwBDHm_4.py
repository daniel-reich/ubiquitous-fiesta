
def show_the_love(lst):
  return [i*0.75+sum(lst)*0.25if i==min(lst) else i*0.75 for i in lst[:]]

