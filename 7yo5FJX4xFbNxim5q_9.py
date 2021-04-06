
def harry(po):
  try:
    top_row = po[0]
    bot_row = po[-1]
  
    lef_col = [r[0] for r in po]
    rig_col = [r[-1] for r in po]
  
    return max([sum(top_row) + sum(rig_col[1:]), sum(lef_col) + sum(bot_row[1:])])
  except IndexError:
    return -1

