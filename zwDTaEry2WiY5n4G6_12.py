
def digital_vowel_ban(n, ban):
  b, n = {'e': '0135789', 'i': '5689', 'o': '0124', 'u': '4'}, str(n)
  t = n.maketrans(dict.fromkeys(b.get(ban,'')))
  n = n.translate(t)
  return 'Banned Number' if n=='' else int(n)

