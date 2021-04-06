
def pad(message):
  a = list(message) + ["lo" for i in range(int((139 - len(message)) / 2))]
  m = "".join(a)
  if len(m) < 140:
      a += ["l"]
  m = "".join(a)
  add = 140 - len(m)
  if add:
      if "lol" in m:
          start = m.index("lol")
          for i in range(add):
              a.insert(start, " ")
  return "".join(a)

