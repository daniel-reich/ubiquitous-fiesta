
def get_best_student(grades):
  winner, score = "", 0
  for i in grades:
    if sum(grades[i]) > score:
      score, winner = sum(grades[i]), i
  return winner

