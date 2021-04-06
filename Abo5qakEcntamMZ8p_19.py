
import string
def gimme_the_letters(spectrum):
    l = string.ascii_letters
    txt = ""
    spectrum = spectrum.split("-")
    num1, num2 = l.find(spectrum[0]), l.find(spectrum[1]) + 1
    for x in l[num1:num2]:
        txt += x
    return txt

