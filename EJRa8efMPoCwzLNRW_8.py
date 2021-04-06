
def dakiti(sentence):
    words = sentence.split()
    n = len(words)
​
    new_sentence = ""
    final_sentence = ""
    for i in range(1, n+1):
        for elem in words:
            if str(i) in elem:
                new_sentence += elem + " "
                break
​
    for i in range(len(new_sentence)-1):
        if new_sentence[i].isdigit():
            pass
        else:
            final_sentence += new_sentence[i]
    return final_sentence

