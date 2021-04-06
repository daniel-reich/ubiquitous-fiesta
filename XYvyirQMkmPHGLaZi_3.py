
def boom_intensity(n):
  if n < 2 :
    return 'boom'
  boom  = 'B'
  for i in range(n) :
    boom += 'o'
  boom += 'm'
  if n % 2 == 0:
    boom += '!'
  if n % 5 == 0:
    boom = boom.upper()
  return boom

