
def gimme_the_letters(spectrum):
  return "".join([chr(ch) for ch in range(ord(spectrum.split("-")[0]), ord(spectrum.split("-")[-1]) + 1)])

