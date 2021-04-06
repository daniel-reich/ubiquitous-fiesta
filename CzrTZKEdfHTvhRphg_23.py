
def mixed_number(frac):
  num, den = int(frac.split("/")[0]), int(frac.split("/")[1])
  if num % den == 0: return str(num // den)   
  else:
    if abs(num+0) >= den:
      if num <0:
        whole, num = abs(num) // den, abs(num) % den
        whole *= -1
      else:
        whole, num = num // den, num % den
    else:
      whole = 0
    while True:
      divided = False
      for i in [2,3,5,7,9,11,13,17,19]:
        if num % i == 0 and den % i == 0:
          num, den = num // i, den // i
          divided = True
          break
      if not divided:
        break       
  if whole == 0:
    return "{}/{}".format(num, den)
  return "{} {}/{}".format(whole, num, den)

