
def is_smooth (sentence) :
    sentence = sentence.split(' ')
​
    for word in range(len(sentence)-1) :
        if sentence[word][-1].lower() != sentence[word+1][0].lower() :
            return False
    
    return True

