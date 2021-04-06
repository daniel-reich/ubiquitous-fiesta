
def simple_encoder(s):
  better = s.lower()
  answer = ""
  for x in better:
    if better.count(x) == 1:
      answer += "["
    else:
      answer += "]"
  return answer

