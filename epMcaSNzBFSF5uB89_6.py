
def currently_winning(scores):
  result = []
  for i in range(len(scores) // 2):
    y = sum(scores[:i*2 +1:2])
    o = sum(scores[1:i*2 +2:2])
    r = 'Y' if y > o else 'O' if y < o else 'T'
    result.append(r)
​
  return result

