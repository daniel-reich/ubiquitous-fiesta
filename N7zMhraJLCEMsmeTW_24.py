
def min_swaps(string):
  first_odd, first_even = [], []
  for i in range(len(string)):
    first_odd += "1" if i % 2 == 0 else "0"
    first_even += "0" if i % 2 == 0 else "1"
  
  diff_f_odd = [1 for a, b in zip(first_odd, list(string)) if a != b]
  diff_f_even = [1 for a, b in zip(first_even, list(string)) if a != b]
​
  return min((sum(diff_f_odd), sum(diff_f_even)))

