
def lets_meet(distance, va, vb):
  seconds = 3600 * distance / (va + vb)
  return '{:0.0f}h {:0.0f}min {}s'.format(
    seconds // 3600,
    seconds % 3600 // 60,
    int(seconds % 3600 % 60)
  )

