
def elasticize(word):
  tempstrleft = ''
  tempstrright = ''
  for cnt in range((len(word)+1)//2):
    tempstrleft += word[cnt] * (cnt + 1)
  for cnt in range((len(word))//2):
    tempstrright += word[-(cnt+1)] * (cnt + 1)
  return tempstrleft + tempstrright[::-1]

