
def worm_length(worm):
  if worm.count('-') == len(worm) and len(worm) > 0:
      return str(len(worm) * 10) + ' mm.'
​
  return "invalid"

