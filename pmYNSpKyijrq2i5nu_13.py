
from itertools import combinations_with_replacement
​
def darts_solver(sections, darts, target):
  permutation_list = []
  sorted_dup_list = []
  string_list = []
  permutation_list.extend(list(combinations_with_replacement(sections,darts)))
  for x in range(0,len(permutation_list)):
    sum_numbers = 0
    string_list = []
    for digit in permutation_list[x]:
      sum_numbers += digit
    if sum_numbers == target:
      string_list = list(map(str, sorted(permutation_list[x])))
      sorted_dup_list.append("-".join(string_list))
  return(sorted_dup_list)

