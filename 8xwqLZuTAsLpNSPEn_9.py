
def award_prizes(names):
  s = sorted(names.values(),reverse=True)
  medals = ['Gold' if names[i]==s[0] else 'Silver' if names[i]==s[1] else 'Bronze' if names[i]==s[2] else 'Participation' for i in names]
  return {k:v for k,v in zip(names,medals)}

