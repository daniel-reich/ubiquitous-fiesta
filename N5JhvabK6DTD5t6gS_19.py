
import re
def markdown(symb):
    def formatting(sentence, word):
        sentence = sentence.split()
        pattern = re.compile(r"\b"+word+r"[.,:;!?]*", re.I)
        for i in range(len(sentence)):
            m = pattern.match(sentence[i])
            if m:
                sentence[i] = symb+m.group(0)+symb
        return " ".join(sentence)
    return formatting

