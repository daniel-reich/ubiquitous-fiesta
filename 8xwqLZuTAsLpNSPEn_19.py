
def award_prizes(names):
  awards, top = ['Gold','Silver','Bronze'], sorted(names.values(), reverse=True)[:3]
  return {i:awards[top.index(names[i])] if names[i] in top else 'Participation' for i in names}

