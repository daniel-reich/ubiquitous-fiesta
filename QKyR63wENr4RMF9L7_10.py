
def tweak_letters(txt, lst):
  letters = "abcdefghijklmnopqrstuvwxyz"
  return "".join([letters[(letters.index(txt[i])+lst[i])%26] for i in range(len(txt))])

