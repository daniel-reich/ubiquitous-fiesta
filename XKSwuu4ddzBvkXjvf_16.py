
def is_prime(number):
    return(([i for i in range(2, number) if number%i == 0] == []) and number>1)
​
def to_values(word):
    sum = 0
    for s in word:
        if ord(s) in range(48, 58):
                sum += ord(s)-48
        elif ord(s) in range(65, 91):
                sum += ord(s)-64
        elif ord(s) in range(97, 123):
                sum += ord(s)-96
    return(sum)
​
def partly_value(words):
    pw = [words[0:i]+words[(i+1):len(words)] for i in range(0, len(words))]
    pv = []
    for s in pw:
        combination = ""
        for t in s:
            combination += t
        pv.append(to_values(combination))
    return(pv)
​
def sentence_primeness(sentence):
    new = ""
    for s in sentence:
        if ord(s) in range(48, 58) or ord(s) in range(65, 91) or ord(s) in range(97, 123):
            new += s
        else:
            new += " "
    words = new.split()
    value = 0
    for word in words:
        value += to_values(word)
    if is_prime(value):
        return("Prime Sentence")
    else:
        outcome = False
        for i in range(0, len(words)):
            outcome = (outcome or is_prime(partly_value(words)[i]))
            if is_prime(partly_value(words)[i]):
                return("Almost Prime Sentence (" + words[i] + ")")
                break
        if outcome == False:
            return("Composite Sentence")

