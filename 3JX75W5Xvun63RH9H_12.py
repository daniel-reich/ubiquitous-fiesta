
def describe_num(n):
  r = ['The','most']
  l = ['','brilliant', 'exciting', 'fantastic', 'virtuous', 'heart-warming', 'tear-jerking', 'beautiful', 'exhilarating', 'emotional', 'inspiring']
  for x in range(1,11):
    if n%x == 0:
      r.append(l[x])
  r.append('number is {}!'.format(n))
  return ' '.join(r)

