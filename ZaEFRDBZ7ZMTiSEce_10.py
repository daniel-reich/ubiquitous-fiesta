
def find_nemo(s):
  for i in s.split():
    if i == 'Nemo':
      return "I found Nemo at " + (str(s.split().index(i)+1) + '!')
  return "I can't find Nemo :("

