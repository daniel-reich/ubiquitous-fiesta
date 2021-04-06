
def currently_winning(scores):
  y_score = scores[::2]
  o_score = scores[1::2]
​
  for i in range(1,len(y_score)):
    y_score[i] = sum(y_score[i-1:i+1])
    o_score[i] = sum(o_score[i-1:i+1])
​
  result = []
  for i in range(len(y_score)):
    if y_score[i] > o_score[i]:
      result.append('Y')
    elif y_score[i] < o_score[i]:
      result.append('O')
    else:
      result.append('T')
​
  return result

