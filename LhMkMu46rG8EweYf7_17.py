
def sort_by_letter(lst):
  return sorted(lst, key = alpha)
​
def alpha(s):
  for i in s: 
    if i.isalpha():
      return i

