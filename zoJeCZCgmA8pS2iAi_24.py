
def func_sort(lst):
  return sorted(lst, key = num_calls)
  
def num_calls(function):
  is_callable = callable(function)
  calls = 0
  while(is_callable):
    function = function()
    calls += 1
    is_callable = callable(function)
  return calls

