
def remix(txt, lst):
  reord = [0]*len(txt)
  for i in range(len(lst)):
    reord[lst[i]] = txt[i]
  return ''.join(reord)

