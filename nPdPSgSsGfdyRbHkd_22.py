
def hacker_speak(txt):
  def code_replacement(ch):
    if ch == 'a':
      return '4'
    elif ch == 'o':
      return '0'
    elif ch == 'e':
      return '3'
    elif ch == 'i':
      return '1'
    elif ch == 's':
      return '5'
    else:
      return ch
      
  return "".join([code_replacement(ch) for ch in txt])

