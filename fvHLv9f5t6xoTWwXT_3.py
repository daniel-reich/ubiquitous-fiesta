
def grab_number_sum(s):
  return sum(int(i) if i.isnumeric() else 0 for i in ''.join(' ' if i.isalpha() else i for i in s).split(' '))

