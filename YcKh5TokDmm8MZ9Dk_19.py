
import re
​
def hidden_anagram(text, phrase):
    text = re.sub("[^a-zA-Z]", "", text).lower()
    phrase = re.sub("[^a-zA-Z]", "", phrase).lower()
​
    p_length = len(phrase)
    sorted_phrase = ''.join(sorted(phrase))
​
    for i in range(len(text) - p_length+1):
        part = ''.join(sorted(text[i:i+p_length]))
        #print(part, ' ', sorted_phrase, ' ', text)
        if part == sorted_phrase:
            return text[i:i+p_length]
​
    return "noutfond"

