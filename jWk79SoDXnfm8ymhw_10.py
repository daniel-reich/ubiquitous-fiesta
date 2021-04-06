
censor = lambda s: ' '.join(['*'*len(word) if len(word)>4 else word for word in s.split()])

