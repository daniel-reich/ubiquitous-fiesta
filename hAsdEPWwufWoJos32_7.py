
import re
​
def no_yelling(phrase):
    x = ""
    yellRegex = re.compile(r"\!+$|\?+$")
    punc = "".join(yellRegex.findall(phrase.split()[-1]))
    if "?" in punc:
        x += "?"
    elif "!" in punc:
        x += "!"
    if len(phrase.split()) == 1:
        return phrase.replace(punc, x)
    else:
        return " ".join(phrase.split()[:-1]) + " " + phrase.split()[-1].replace(punc, x)

