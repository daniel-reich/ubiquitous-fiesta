
bet = "abcdefghijklmnopqrstuvwxyz"
BET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def caesar_cipher(s, k):
  ans = ""
  for letter in s:
    if letter in BET:
      i = BET[(BET.index(letter,0) + k) % 26]
    elif letter in bet:
      i = bet[(bet.index(letter,0) + k) % 26]
    else:
      i = letter
    ans += i
  return ans

