
def possibly_perfect(key, answers):
  
  #remove underscores from key and associated index from answers, working backwards
  i = len(key)-1
  while i >= 0:
    if key[i] == '_':
      del key[i]
      del answers[i]
    i -= 1
​
  #count is incremented/decrementd for correct/incorrect answers
  count = 0
  for i in range(len(key)):
    if key[i] == answers[i]:
      count += 1
    else:
      count -= 1
​
  #if abs(count) is the same as len(key), either all answers are correct or all answeres are incorrect
  return abs(count) == len(key)

