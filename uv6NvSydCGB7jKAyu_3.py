
def is_parsel_tongue(sentence):
  return len(list(filter(lambda x: x.lower().count('ss')>=1 or x.lower().count('s')==0,sentence.split())))==len(sentence.split())

