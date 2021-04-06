
def every_some(test, val, a, b, c, d, e):
  lst = []
  for x in 'abcde':
    lst.append(eval(str(x)+test))
  return all(lst) if val=='everybody' else any(lst)

