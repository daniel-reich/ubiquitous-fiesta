
import numpy as np
def majority_vote(lst):
  length_of_list = len(lst)
  uniq_list= np.unique(lst)
  for x in uniq_list:
    if lst.count(x) > length_of_list/2:
      return x

