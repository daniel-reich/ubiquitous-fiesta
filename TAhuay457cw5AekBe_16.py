
def monkey_talk(txt):
  return (" ".join(["eek" if i[0] in 'aeiouAEIOU' else "ook" for i in txt.split()])).capitalize() + "."

