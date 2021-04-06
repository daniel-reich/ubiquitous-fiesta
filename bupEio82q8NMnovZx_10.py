
def track_robot(instructions):
  esquerda, direita, acima, abaixo = (0, 0, 0, 0)
  for i in instructions:
    if (i.split(' ')[0]) == 'left':
      esquerda += int(i.split(' ')[1]) * (-1)
    if (i.split(' ')[0]) == 'right':
      direita += int(i.split(' ')[1])
    if (i.split(' ')[0]) == 'up':
      acima += int(i.split(' ')[1])
    if (i.split(' ')[0]) == 'down':
      abaixo += int(i.split(' ')[1]) * (-1)
  return [direita + esquerda, acima + abaixo]

