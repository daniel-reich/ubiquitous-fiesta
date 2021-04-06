
def award_prizes(names):
  participants = sorted(names.keys(),key = lambda x: names[x],reverse = True)
  prizes = {x: 'Participation' for x in names.keys()}
  prizes[participants[0]] = 'Gold'
  prizes[participants[1]] = 'Silver'
  prizes[participants[2]] = 'Bronze'
  return prizes

