
vowels = "aeiouAEIOU"
letters = [chr(k) for k in range(65, 91)] + [chr(k) for k in range(97, 123)]
​
def translate_word(word):
    if len(word) == 0:
        return word
    first_upper = 'A' <= word[0] <= 'Z'
    if word[0] not in vowels:
        while word[0] not in vowels:
            word = word[1:] + word[0].lower()
        word += "ay"
        if first_upper:
            word = word[0].upper() + word[1:]
    else:
        word += "yay"
    return word
  
​
def translate_sentence(sentence):
    if sentence == "":
        return ""
    txt = sentence
    pig = ""
    word = ""
    for char in txt:
        if char in letters:
            word += char
        else:
            pig += translate_word(word)
            word = ""
            pig += char
    if word != "":
        pig += translate_word(word)
    pig = pig[0].upper() + pig[1:]
    return pig

