
def hidden_anagram(text, phrase):
    text = "".join([x.lower() for x in text if x.isalpha()])
    phrase = "".join(phrase.lower().split())
    lt, lp = len(text), len(phrase)
    for x in range(lt - lp + 1):
        if sorted(text[x : x + lp ]) == sorted(phrase):
            return text[x : x + lp]
    return "noutfond"

