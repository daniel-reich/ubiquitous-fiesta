
def max_occur(text):
  a=text.count(max(text,key=lambda x:text.count(x)))
  if a>1:
    return list(set([i for i in text if text.count(i)==a]))
  return "No Repetition"

