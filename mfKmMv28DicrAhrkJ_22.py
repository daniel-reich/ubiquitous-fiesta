
def hex_color_mixer(colors):
  for i in range(len(colors)):
    colors[i] = [int(colors[i][j:j+2],16) for j in range(1,7,2)]
  return '#'+''.join([hex(round_half_up(sum(i)/len(i)))[2:].upper().zfill(2) for i in zip(*colors)])
​
def round_half_up(n):
  if n - int(n) == 0.5:
    n += 0.1
  return round(n)

