
def hidden_anagram(text, phrase):
    text = ''.join([char.lower() for char in text if char.isalpha()])
    chunk_len = len(phrase.replace(' ', ''))
    chunks = [text[i:i+chunk_len] for i in range(0, len(text)-chunk_len+1)]
    chunk_dict = {chunk: generate_letter_list(chunk) for chunk in chunks}
    phrase_lst = generate_letter_list(phrase)
    matches = [chunk for chunk, chunk_lst in chunk_dict.items() if chunk_lst == phrase_lst]
    if not matches:
        return "noutfond"
    else:
        return matches[-1]
​
def generate_letter_list(word):
    char_list = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    return [len([x for x in word if x.lower() == l]) for l in char_list]

