
def boom_intensity(n):
  if n < 2:
    return 'boom'
  return 'B' + ('oO'[n%5==0])*n + 'mM'[n%5==0] + '!'*(1-n%2)

