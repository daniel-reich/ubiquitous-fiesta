
def gimme_the_letters(spectrum):
  abc = "abcdefghijklmnopqrstuvwxyz"
  start = abc.find(spectrum[0].lower())
  end = abc.find(spectrum[-1].lower())
  return abc[start:end+1] if spectrum.islower() else abc[start:end+1].upper()

