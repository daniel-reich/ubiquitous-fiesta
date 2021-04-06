
import itertools
​
def darts_solver(sections, darts, target):
  score_list = list(itertools.product(sections, repeat=darts))
  solution_list = []
  score_set = []
  s_set = []
  
  for score in score_list:
    s = [x for x in score]
    s.sort()
    if s not in s_set:
      s_set.append(s)
      score_set.append(score)
      
  for score in score_set: 
    if sum(score) == target:
      s = [str(x) for x in score]
      score_string = "-".join(s)
      solution_list.append(score_string)
      
  return solution_list

