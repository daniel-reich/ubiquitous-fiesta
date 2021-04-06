
def worm_length(worm):
  if len(worm) != worm.count('-') or not worm:
    return 'invalid'
  return str(len(worm)*10) + ' mm.'

