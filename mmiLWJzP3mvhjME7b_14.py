
def divisible(DJ, Khaled = 'S0'):
  WeTheBest = {
      'S0' : {0 : 'S0',
          1 : 'S1'},
      'S1' : {0 : 'S2',
          1 : 'S0'},
      'S2' : {0 : 'S1',
          1 : 'S2'}}
  def Another(One):
    return divisible(One, Khaled)
  if DJ == 'state': return Khaled
  if DJ == 'stop' : return 'accept' if Khaled == 'S0' else 'reject'
  Khaled = WeTheBest[Khaled][DJ]
  return Another

