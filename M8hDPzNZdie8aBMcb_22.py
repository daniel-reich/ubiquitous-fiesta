
def count_substring(txt):
  return sum(
    txt[index:].count('X')
    for index, letter in enumerate(txt)
    if letter is 'A'
  )

