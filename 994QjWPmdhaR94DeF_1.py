
def get_birthday_cake(n,a):
  c=('#','*')[a%2]
  s='{2} {1} Happy Birthday {0}! {1} {2}'.format(n,a,c)
  return[c*len(s),s,c*len(s)]

