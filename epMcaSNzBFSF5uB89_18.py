
def currently_winning(scores):
  m=scores[::2]
  o=scores[1::2]
  return ['Y' if sum(m[:x+1])>sum(o[:x+1]) else 'T' if sum(m[:x+1])==sum(o[:x+1]) else 'O' for x in range(len(m))]

