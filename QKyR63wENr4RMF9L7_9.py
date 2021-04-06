
def tweak_letters(txt, lst):
  alpha = "abcdefghijklmnopqrstuvwxyz"
  return "".join([alpha[((b + alpha.find(a)) % 26)] for a, b in zip(txt, lst)])

