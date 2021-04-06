
def grab_number_sum(s):
  for i in 'abcdefghijklmnopqrstuvwxyz': s=s.replace(i,' ')
  return sum(map(int,s.split()))

