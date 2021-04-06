
def dice_score(throw):
    throw = sorted(throw)
    counter = 0
    if throw.count(1) == 3:
      counter += 1000
    elif throw.count(6) == 3:
      counter += 600
    elif throw.count(5) == 3:
      counter += 500
    elif throw.count(3) == 3:
      counter += 300
    elif throw.count(2) == 3:
      counter += 200
    elif throw.count(1) == 1:
      counter += 100
    elif throw.count(5) != 1 and throw.count(4) == 3:
      counter += 400
    elif throw.count(5) == 1 and throw.count(4) == 3:
      counter += 450
    return counter

