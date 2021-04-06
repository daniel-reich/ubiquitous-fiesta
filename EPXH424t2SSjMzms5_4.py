
def remix(txt, lst):
  return "".join(sorted(txt, key=lambda _: lst.pop(0)))

