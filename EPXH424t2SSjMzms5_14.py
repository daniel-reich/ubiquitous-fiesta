
def remix(txt, lst):
  a=[1]*len(txt)
  for i in range(len(txt)):
    a[lst[i]]=txt[i]
  return ''.join(a)

