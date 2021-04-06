
def monkey_talk(txt):
  s = " ".join("eek" if x[0] in "aeiouAEIOU" else "ook" for x in txt.split(" "))
  return "{0}{1}.".format(s[0].upper(), s[1:])

