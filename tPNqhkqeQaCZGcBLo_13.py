
def determine_who_cursed_the_most(d):
  me=sum(d[x]['me'] for x in d)
  sp=sum(d[x]['spouse'] for x in d)
  if me>sp:
    return "ME!"
  elif me<sp:
    return "SPOUSE!"
  else:
    return "DRAW!"

