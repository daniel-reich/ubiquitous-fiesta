
def digital_vowel_ban(n, ban):
  d={'1': "one", '2': "two", '3': "three", '4': "four", '5': "five", '6': "six", '7': "seven", '8': "eight", '9': "nine", '0': "zero"}
  return "Banned Number" if [i for i in str(n) if ban not in d[i]]==[] else int("".join([i for i in str(n) if ban not in d[i]]))

