
import re
​
​
def sentence_searcher(txt, word):
    sentences = re.split(r"(?<=\w\.)\s", txt)
    for i, s in enumerate(sentences):
        if word.lower() in s.lower():
            return sentences[i]
    return ""

