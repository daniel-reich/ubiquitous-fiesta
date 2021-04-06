
def truncate(txt, length):
  words = txt.split(' ')
  cum_len = [0]
  cum_len.append(len(words[0]))
  for word in words [1:]:
    cum_len.append(len(word)+cum_len[-1]+1)
  result = [x for x in cum_len if x <= length]
  return ' '.join(words[:len(result)-1])

