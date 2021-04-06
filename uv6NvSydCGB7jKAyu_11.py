
def is_parsel_tongue(sentence):
  sentsplit = sentence.split(" ")
  answer = False
  for word in sentsplit:
    if 's' not in word.lower() or 'ss' in word.lower():
      answer = True
    else:
      answer = False
      break
  return answer

