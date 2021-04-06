
def determine_who_cursed_the_most(d):
  me_score = 0
  spouse_score = 0
  for eachround in d:
    spouse_score += d[eachround]['spouse']
    me_score += d[eachround]['me']
  return 'ME!' if me_score > spouse_score else 'SPOUSE!' if spouse_score > me_score else 'DRAW!'

