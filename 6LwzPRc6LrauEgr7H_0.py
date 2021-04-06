
def worm_length(worm):
  return ('{} mm.'.format(10 * len(worm)) if
    set(worm) == {'-'} else 'invalid')

