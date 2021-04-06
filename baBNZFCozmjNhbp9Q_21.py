
def box_seq(step):
  if step == 0:
    return 0
  elif step % 2:
    return box_seq(step-1) +3
  else:
    return box_seq(step-1) - 1

