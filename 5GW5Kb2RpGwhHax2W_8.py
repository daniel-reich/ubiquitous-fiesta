
def pop_up(lst):
  if not lst: return []
  return lst.pop(0)
​
def pop_right(lst):
  if not lst: return []
  return [row.pop() for row in lst]
​
def pop_down(lst):
  if not lst: return []
  return lst.pop()[::-1]
​
def pop_left(lst):
  if not lst: return []
  return [row.pop(0) for row in lst][::-1]
​
def append(lst, result):
  if lst:
    [result.append(x) for x in lst]
​
def spiral_transposition(lst):
  result = []
  while lst:
    append(pop_up(lst),result)
    append(pop_right(lst),result)
    append(pop_down(lst),result)
    append(pop_left(lst),result)
  return result

