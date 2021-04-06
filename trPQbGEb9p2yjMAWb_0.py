
def every_some(test, m, *lst):
  return (all if m[0] == 'e' else any)(eval(str(i)+test) for i in lst)

