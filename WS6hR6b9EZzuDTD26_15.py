
def no_duplicate_letters(phrase):
    phrase = phrase.split()
    for word in phrase:
        for i in range(len(word)):
            if word[i] in word[i+1::]:
                return False
    else:
        return True
​
​
print(no_duplicate_letters("Look before you leap"))

