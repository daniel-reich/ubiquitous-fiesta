
def total_points(guesses, word):
  return sum(point[len(i)] for i in guesses if len(list(j for j in i if i.count(j) <= word.count(j)))==len(i)) 
point = {3:1,4:2,5:3,6:54}

