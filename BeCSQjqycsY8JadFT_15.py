
def recur_index(txt, viewed = "", index =0):
  try:
    if txt[index] in viewed:
      return {txt[index]: [viewed.index(txt[index]), index]}
    else:
      return recur_index(txt, viewed + txt[index], index +1)
  except:
    return {}

