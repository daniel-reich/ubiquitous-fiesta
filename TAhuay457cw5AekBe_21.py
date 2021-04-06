
def monkey_talk(txt):
  t=[]
  for x in txt.split():
    if x[0].lower() in "aeiou":
      t.append("eek")
    else:
      t.append("ook")
  return "{}.".format(" ".join(t)).capitalize()

