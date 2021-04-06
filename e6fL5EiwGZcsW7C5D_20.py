
def alph_num(txt):
  alphas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  pos = range(len(alphas))
  alphapos = zip(alphas, pos)
  
  for alpha, num in alphapos:
    txt = txt.replace(alpha, str(num)+' ') 
    
  return txt[:-1]

