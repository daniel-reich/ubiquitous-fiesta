
import itertools
​
def dice_roll(dice, number):
​
  dict, fina = [], []
  suma = 0
​
  if dice == 1:
    return 1
  
  for i in range(0, dice):
    dict.append([])
    for j in range(0, 6):
      dict[i].append(j+1)
​
  all_possibilites = list(itertools.product(*dict))
​
  for i in range(len(all_possibilites)):
    for j in range(len(all_possibilites[i])):
      suma = suma + all_possibilites[i][j]
    if suma == number:
      fina.append(all_possibilites[i])
    suma = 0
​
  return len(fina)

