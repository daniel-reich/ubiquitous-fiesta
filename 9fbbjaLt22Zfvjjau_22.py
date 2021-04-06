
import string
def paul_cipher(txt):
    output = ""
    firstalpha = True
    letters = string.ascii_lowercase
    for i in range(len(txt)):
        if txt[i].isalpha() and firstalpha:
            output += txt[i].upper()
            firstalpha = False
            prevletterindex = letters.index(txt[i].lower())
        elif txt[i].isalpha():
            ciphindex = letters.index(txt[i].lower()) + prevletterindex + 1
            if ciphindex >= 26:
                ciphindex -= 26
            output += letters[ciphindex].upper()
            prevletterindex = letters.index(txt[i].lower())
        else:
            output += txt[i]
    return output

