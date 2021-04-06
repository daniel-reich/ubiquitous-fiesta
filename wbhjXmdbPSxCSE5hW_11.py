
def sigilize(des):
  d = des.upper().replace(' ', '')
  return ''.join(d[x] for x in range(len(d)) if d[x] not in 'AEIOUaeiou'\
                                                and d[x] not in d[x+1::])

