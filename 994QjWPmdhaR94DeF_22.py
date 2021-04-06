
def get_birthday_cake(name, age):
  m = '#*'[age % 2].join(["", " {} Happy Birthday {}! {} ".format(age, name, age), ""])
  return ['#*'[age % 2]*len(m), m, '#*'[age % 2]*len(m)]

