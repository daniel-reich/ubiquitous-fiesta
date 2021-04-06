
def gold_distribution(gold):
  mubashir_turn = True
  matt_turn = False
  mubashir_total = 0
  matt_total = 0
  while len(gold) > 0:
    far_left = gold[0]
    far_right = gold[-1]
    if far_left == far_right and mubashir_turn:
      del gold[0]
      mubashir_total += far_left
      mubashir_turn = False
      matt_turn = True
    elif far_left == far_right and matt_turn:
      del gold[0]
      matt_total += far_right
      matt_turn = False
      mubashir_turn = True
    elif far_left > far_right and mubashir_turn:
      del gold[0]
      mubashir_total += far_left
      mubashir_turn = False
      matt_turn = True
    elif far_left > far_right and matt_turn:
      del gold[0]
      matt_total += far_left
      mubashir_turn = True
      matt_turn = False
    elif far_right > far_left and mubashir_turn:
      del gold[-1]
      mubashir_total += far_right
      mubashir_turn = False
      matt_turn = True
    elif far_right > far_left and matt_turn:
      del gold[-1]
      matt_total += far_right
      mubashir_turn = True
      matt_turn = False
  return [mubashir_total,matt_total]

