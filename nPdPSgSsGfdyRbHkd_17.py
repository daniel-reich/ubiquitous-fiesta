
def hacker_speak(txt):
  for i in range(5):
      txt = txt.replace('aeios'[i], '43105'[i])
  return txt

