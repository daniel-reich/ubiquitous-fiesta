
def guess_score(code, guess):
  res_dict={"black":0,"white":0}
  for index in range(len(code)):
    if code[index]==guess[index]:
      res_dict["black"]+=1
      code=code[:index]+"0"+code[index+1:]
  res_dict["white"]=len(set(guess).intersection(code))
  return res_dict

