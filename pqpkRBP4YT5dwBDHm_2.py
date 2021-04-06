
def show_the_love(lst):
  return [i*0.75 if i != min(lst) else i + sum(i*0.25 for i in lst if i != min(lst)) for i in lst]

