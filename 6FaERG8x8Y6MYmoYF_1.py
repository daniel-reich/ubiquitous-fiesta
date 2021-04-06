
def dice_score(throw):
  one = 0
  two = 0
  three = 0
  four = 0
  five = 0
  six = 0
  score = 0
  for num in throw:
    if num == 1:
      one+=1
    if num == 2:
      two+=1
    if num == 3:
      three+=1
    if num == 4:
      four+=1
    if num == 5:
      five+=1
    if num == 6:
      six+=1
  if one == 3:
    score += 1000
  if one ==1:
    score +=100
  if six == 3:
    score += 600
  if five == 3:
    score += 500
  if four == 3:
    score += 400
  if three == 3:
    score += 300
  if two == 3:
    score += 200
  if five == 1:
    score += 50
  return (score)

