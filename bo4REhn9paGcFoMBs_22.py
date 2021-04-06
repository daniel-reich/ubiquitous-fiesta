
def age_difference(ages):
  if[max(ages)-i for i in sorted(ages,reverse=True)[0:2]][1]==0:return "No age difference between spouses."
  if[max(ages)-i for i in sorted(ages,reverse=True)[0:2]][1]==1:return '{} year'.format([max(ages)-i for i in sorted(ages,reverse=True)[0:2]][1])
  return '{} years'.format([max(ages)-i for i in sorted(ages,reverse=True)[0:2]][1])

