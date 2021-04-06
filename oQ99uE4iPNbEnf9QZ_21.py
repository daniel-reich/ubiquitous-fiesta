
def no_perms_digits(number):
  NewNum = 1
  for i in range(number):
    NewNum = NewNum * (i+1)
  for i in range(len(str(NewNum))):
    FinalNum = i + 1
  print("The",number,"unique items can be arranged in",NewNum,"different ways and the number",NewNum,"has",FinalNum,"digits")
  return FinalNum

