
def parse_roman_numeral(num):
  ans = 0
  while num:
    if num[0] == "M":
      ans+= 1000
      num = num[1:]
    elif num[:2] == "CM":
      ans+=900
      num = num[2:]
    elif num[0] == "D":
      ans+= 500
      num = num[1:]
    elif num[:2] == "CD":
      ans+=400
      num = num[2:]
    elif num[:1] == "C":
      ans+=100
      num = num[1:]
    elif num[:2] == "XC":
      ans+=90
      num = num[2:]
    elif num[:1] == "L":
      ans+=50
      num = num[1:]
    elif num[:2] == "XL":
      ans+=40
      num = num[2:]
    elif num[:1] == "X":
      ans+=10
      num = num[1:]
    elif num[:2] == "IX":
      ans+=9
      num = num[2:]
    elif num[:1] == "V":
      ans+=5
      num = num[1:]
    elif num[:2] == "IV":
      ans+=4
      num = num[2:]
    else:
      ans += len(num)
      num = ''
  return ans

