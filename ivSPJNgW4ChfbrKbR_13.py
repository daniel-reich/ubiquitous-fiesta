
def soroban(frame):
  return int(frame[0].replace('|', '5').replace('O', '0')) + \
    sum([int(frame[i].replace('|', str(i-3)).replace('O', '0')) for i in range(4, len(frame))])

