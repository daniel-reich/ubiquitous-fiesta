
def guess_sequence(n):
  
  answer = 90
  addition = 150
  
  added = 1
  required = n
  
  while (added < required):
    answer += addition
    addition += 60
    added += 1
    
  return answer

