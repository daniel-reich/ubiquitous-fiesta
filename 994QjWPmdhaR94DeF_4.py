
def get_birthday_cake(name, age):
  s1 = ['*' if age%2 else '#'][0]
  s2 = ['{} {} Happy Birthday {}! {} {}'.format(s1[0], age, name, age, s1[0])]
  s3 = ['*' if age%2 else '#'][0]
  return [s1*len(s2[0])]+s2+[s3*len(s2[0])]

