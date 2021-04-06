
def show_the_love(lst):
 return [i*0.75 if i != min(lst) else i+sum([j*0.25 for j in lst if j != min (lst)]) for i in lst]

