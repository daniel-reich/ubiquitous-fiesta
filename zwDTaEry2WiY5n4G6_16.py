
def digital_vowel_ban(n, ban):
  dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
          7: 'seven', 8: 'eight', 9: 'nine', 0: 'zero'}
  num = ''.join(i for i in str(n) if ban not in dict[int(i)])
  return 'Banned Number' if len(num) == 0 else int(num)

