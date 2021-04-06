
from itertools import takewhile
def final_result(lst):
  block = find_block(lst)
  while block:
    lst = remove_block(lst, block)
    block = find_block(lst)
  return lst
​
def find_block(lst):
  for i, c1 in enumerate(lst):
    group = list(takewhile(lambda c: c==c1, lst[i+1:]))
    if group:
      return i, group
​
def remove_block(lst, block):
  i, group = block
  return lst[:i] + lst[i+len(group)+1:]

