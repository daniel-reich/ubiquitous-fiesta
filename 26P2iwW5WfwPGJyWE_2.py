
def possibly_perfect(key, ans):
  correct = [k == a for k,a in zip(key,ans) if k != '_']
  return all(correct) or not any(correct)

