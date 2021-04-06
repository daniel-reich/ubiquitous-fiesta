
def find_nemo(sentence):
  s = sentence.split()
  for i in range(len(s)):
    if s[i] == 'Nemo':
      return 'I found Nemo at ' + str(i + 1) + '!'
  return "I can't find Nemo :("

