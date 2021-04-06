
def hacker_speak(txt):
  return txt.translate({ord(i): v for i, v in zip('aeios', '43105')})

