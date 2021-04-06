
def pig_latin_sentence(sentence):
    words = sentence.strip().lower().split()
    new_words = []
    for word in words:
        if word[0] in 'aeiou':
            new_words.append(word+'way')
        else:
            vowel_pos=0
            for let in word:
                if let not in 'aeiou':
                    vowel_pos = vowel_pos+1
                else:
                    break
            new_words.append(word[vowel_pos:] + word[:vowel_pos] + 'ay')
    return ' '.join(new_words)

