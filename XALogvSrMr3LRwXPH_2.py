
def is_shuffled_well(lst):
  txt = '12345678910 10987654321'
  return all(''.join(str(d) for d in i) not in txt for i in zip(lst, lst[1:], lst[2:]))

