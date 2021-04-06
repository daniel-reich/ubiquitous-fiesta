
def dashed(txt):
  return "".join([i if i not in 'aeiouAEIOU' else "-"+i+"-" for i in list(txt)])

