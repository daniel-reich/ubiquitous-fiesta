
hangman = lambda phrase, lst : "".join("-" if ch.isalpha() and ch.lower() not in lst else ch for ch in phrase)

