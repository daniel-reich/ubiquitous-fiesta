
def stmid(string):
  return ''.join([letter[int(len(letter)/2)] if len(letter)%2 else letter[0] for letter in string.split()])

