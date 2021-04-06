
def how_bad(n):
  hbad = []
  binary = '{0:0b}'.format(n)
  if binary.count('1') % 2 == 0:
    hbad.append('Evil') 
  elif binary.count('1') % 2 != 0:
    hbad.append('Odious')
  if binary.count("1") > 1:
    if binary.count("1") == 2:
      hbad.append('Pernicious')
    else:
      for i in range(2, binary.count("1")):
        if binary.count("1") % i == 0:
          break
        else:
          if 'Pernicious' not in hbad:
            hbad.append('Pernicious')
          else:
            break
  return hbad

