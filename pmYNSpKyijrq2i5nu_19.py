
import itertools
def darts_solver(sections, darts, target):
  final = []
  final_num = []
  longlist = list(itertools.product(sections, repeat=darts))
  for i in longlist:
    i = list(i)
    i.sort()
    if sum(i) == target:
      if i not in final:
        str_i = str(i).strip('[').strip(']').replace(' ','').replace(',','-')
        final.append(i)
        final_num.append(str_i)
  
  return final_num

