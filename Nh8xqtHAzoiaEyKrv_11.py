
import re
def correct_sentences(s):
    res = re.sub(r"( [A-Z])", r".\1", re.sub("\s+", " ", s.strip()))
    return res[0].upper() + res[1:] + "."

