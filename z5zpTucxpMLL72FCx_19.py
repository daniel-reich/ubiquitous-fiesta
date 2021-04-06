
def grab_city(txt):
  return ''.join(txt[k] for k in range(txt.rfind('[')+1,txt.rfind(']')))

