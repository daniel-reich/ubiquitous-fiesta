
def clean_up_list(lst):
  even = lambda n: n % 2 == 0
  
  even_nums = [int(n) for n in lst if even(int(n)) == True]
  odd_nums = [int(n) for n in lst if even(int(n)) == False]
  
  return [even_nums, odd_nums]

