
import itertools
def darts_solver(sections, darts, target):
  combinations = list(itertools.combinations_with_replacement(sections, darts))
  valid = [val for val in combinations if sum(val) == target]
​
  out =["-".join(str(c) for c in val) for val in valid] 
# for val in valid:
#   accept = "-".join(str(c) for c in val)
#   out.append(accept)
    
  return out

