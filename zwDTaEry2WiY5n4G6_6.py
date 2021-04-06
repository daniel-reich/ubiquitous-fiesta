
def digital_vowel_ban(n, ban):
  ref = ['zero', 'one', 'two', 'three', 'four','five','six','seven','eight','nine']
  n = [int(i) for i in str(n)]
  new = ''.join([str(ref.index(j)) for j in [ref[i] for i in n if ban not in ref[i]]])
  try:
    return int(new)
  except:
    return 'Banned Number'

