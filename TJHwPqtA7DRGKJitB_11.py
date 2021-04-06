
def is_prob_matrix(lst):
  return len(lst)==len(lst[0]) and all(0<=number<=1 for e in lst for number in e) and all(sum(e)==1 for e in lst)

