
def win_check(match):
​
  if match[0] == match[1]:
    return "Tie"
  if match[0] =="P" and match[1]=="R":
    return True
  if match[0] =="R" and match[1]=="S":
    return True
  if match[0] =="S" and match[1]=="P":
    return True
​
​
  if match[0] =="P" and match[1]=="S":
    return False
  if match[0] =="R" and match[1]=="P":
    return False
  if match[0] =="S" and match[1]=="R":
    return False
  
def calculate_score(games):
  score_Abi=0
  score_Ben=0
  for i in games:
    if win_check(i)==True:
      score_Abi+=1
    if win_check(i)==False:
      score_Ben+=1
    if win_check(i) =="Tie":
      pass
  
  
  if score_Abi>score_Ben:
    return "Abigail"
  if score_Abi<score_Ben:
    return "Benson"
  else:
    return "Tie"

