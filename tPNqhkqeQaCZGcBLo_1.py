
def determine_who_cursed_the_most(d):
  s=sum(v['me']-v['spouse']for v in d.values())
  return('DRAW!',('SPOUSE!','ME!')[s>0])[s!=0]

