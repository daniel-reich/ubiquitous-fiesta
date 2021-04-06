
def average_word_length(txt):
  import re, string
  regex = re.compile('[%s]' % re.escape(string.punctuation))
  res_str = regex.sub('', txt)
  arry = res_str.split(' ')
  return round(sum(len(i) for i in arry)/len(arry), 2)

