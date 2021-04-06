
def x_pronounce(sentence):
    sentence_list=sentence.split(" ")
    modified_sentence=""
    
    for word in sentence_list:
        if "x" in word:
            if len(word) == 1:
                word = word.replace("x", "ecks")
​
            elif word.index("x") == 0:
                word = word.replace("x", "z")
​
            else:
                word = word.replace("x", "cks")
        modified_sentence = modified_sentence.lstrip() + " " + word
        
    return modified_sentence

