
def box_seq(step):
  if step == 0:
    return 0
  else:
    if step % 2 == 0:
      return step
    else:
      return step + 2

