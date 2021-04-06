
def hidden_anagram(text, phrase):
    letters_phrase = sorted([c.lower() for c in phrase if str.isalpha(c)])
    letters_text = [c.lower() for c in text if str.isalpha(c)]
    len_phrase = len(letters_phrase)
    for i in range(len(letters_text) - len_phrase + 1):
        if sorted(letters_text[i:i+len_phrase]) == letters_phrase:
            return "".join(letters_text[i:i+len_phrase])
    return 'noutfond'

