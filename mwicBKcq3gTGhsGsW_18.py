
def make_word_riddle(s):
  spl = s.lower().split("in")
  final = list(spl[1])
  final.insert(1,spl[0])
  return "".join(final).upper()

