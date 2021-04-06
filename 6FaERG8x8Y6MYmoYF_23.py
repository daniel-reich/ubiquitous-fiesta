
def dice_score(throw):
  c_o = 0
  c_t = 0
  c_th = 0
  c_f = 0
  c_fi = 0
  c_s = 0
  for num in throw:
    if num == 1:
      c_o+=1
    elif num == 2:
      c_t+=1
    elif num == 3:
      c_th+=1
    elif num == 4:
      c_f+=1
    elif num == 5:
      c_fi+=1
    else:
      c_s+=1
  score = 0
  
  if c_o == 3:
    score = score + 1000
  elif c_o == 1:
    score = score + 100
  
  if c_t == 3:
    score = score + 200
    
  if c_th == 3:
    score = score + 300
  
  if c_f == 3:
    score = score + 400
  
  if c_fi == 3:
    score = score + 500
  elif c_fi == 1:
    score = score + 50
  
  if c_s == 3:
    score = score + 600
  return score

