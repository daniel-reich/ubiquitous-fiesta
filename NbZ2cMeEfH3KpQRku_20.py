
def percentage_happy(numbers):
  # Scoring
  score = {'happy': 0, 'unhappy': 0}
  # First element
  if(numbers[0] == numbers[1]):
    score['happy'] += 1
  else:
    score['unhappy'] += 1
  # Last element
  if(numbers[-1] == numbers[-2]):
    score['happy'] += 1
  else:
    score['unhappy'] += 1
  # Remaining elements
  for i in range(1, len(numbers)-1):
    if(numbers[i] == numbers[i-1] or numbers[i] == numbers[i+1]):
      score['happy'] += 1
    else:
      score['unhappy'] += 1
  return score['happy']/(score['happy']+score['unhappy'])

