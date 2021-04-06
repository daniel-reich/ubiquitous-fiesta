
def make_word_riddle(s):
  s = s.lower()
  
  before_in = s.split('in')[0]
  after_in = s.split('in')[1]
  
  final = after_in[0] + before_in + after_in[1:]
  
  return final.upper()

