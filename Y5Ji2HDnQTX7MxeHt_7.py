
def snakefill(n):
  area = n**2
  pow = 0
  while 2**pow <= area:
    pow += 1
  return pow-1

