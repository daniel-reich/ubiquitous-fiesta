
def concat(*args):
  answer = []
  for arg in args:
    for item in arg:
      answer.append(item)
  return answer

