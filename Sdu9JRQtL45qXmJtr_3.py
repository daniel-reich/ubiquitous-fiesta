
def happy_birthday(age):
  base = age // 2
  return 'Mubashir is just 2{}, in base {}!'.format(
    ('0', '1')[age % 2], 
    base,
  )

