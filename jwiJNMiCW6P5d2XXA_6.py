
vowels = 'aeiuoAEIUO'
​
def does_rhyme(txt1, txt2):
    
    lastword_of_sentence1 = list(txt1.lower().split())[-1]
    lastword_of_sentence2 = list(txt2.lower().split())[-1]
​
    #find vowels of last word of first sentence
    vowels_in_lastword_of_sentence1 = []
    for i in lastword_of_sentence1:
        if i in vowels:
            vowels_in_lastword_of_sentence1.append(i)
        else: pass
    
    #find vowels of last word of second sentence
    vowels_in_lastword_of_sentence2 = []
    for i in lastword_of_sentence2:
        if i in vowels:
            vowels_in_lastword_of_sentence2.append(i)
        else: pass
​
    if set(vowels_in_lastword_of_sentence1) == set(vowels_in_lastword_of_sentence2):
        return True
    else: 
        return False

