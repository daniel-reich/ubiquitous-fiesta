
def seesaw(num):
  even_left_num = str(num)[0:(len(str(num)))//2]
  even_right_num = str(num)[len(str(num))//2:]
  odd_left_num = str(num)[0:(len(str(num)))//2]
  odd_right_num = str(num)[len(str(num))//2+1:]
  if num == None:
    return "balanced"
  elif len(str(num))%2 == 0:
    if even_left_num > even_right_num:
      return "left"
    elif even_left_num < even_right_num:
      return "right"
    else:
      return "balanced"
  elif len(str(num))%2 != 0:
    if odd_left_num > odd_right_num:
      return "left"
    elif odd_left_num < odd_right_num:
      return "right"
    else:
      return "balanced"

