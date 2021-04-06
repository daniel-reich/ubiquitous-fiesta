
def look_and_say(n):
  n = str(n)
  length = len(n)
  if length % 2 == 1:
    return 'invalid'
  else:
    answer_so_far = ''
    i = 0
    while i < length:
      answer_so_far += n[i+1] * int(n[i])
      i += 2
  return int(answer_so_far)

