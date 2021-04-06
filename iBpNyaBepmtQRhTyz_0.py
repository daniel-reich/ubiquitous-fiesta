
def stripped(sentence):
    return sentence.lower().translate({ord(c): None for c in ' !@#$.'})
def filled(sentence, keyword_len):
    final_size = len(sentence)+(keyword_len-len(sentence)%keyword_len)%keyword_len
    return sentence.ljust(final_size, 'x')
def chunks(sentence, size):
    return [sentence[idx:idx+size] for idx in range(0, len(sentence), size)]
def cipher(msg, keyword):
    unsorted = chunks(filled(stripped(msg), len(keyword)), len(keyword))
    sorted_indexed = sorted(enumerate(zip(*unsorted)), key= lambda k: keyword[k[0]])
    return ''.join([''.join(tupl) for index, tupl in sorted_indexed])
def decipher(msg, keyword):
    unsorted = chunks(msg, len(msg)//len(keyword))
    sorting = [idx for idx,val in sorted(enumerate(keyword), key=lambda k: k[1])]
    sorted_indexed = [[sub[sorting.index(idx)] for idx in range(len(sub))] for sub in zip(*unsorted)]
    return ''.join([''.join(chunk) for chunk in sorted_indexed])
def c_cipher(msg, keyword):
    return cipher(msg, keyword) if ' ' in msg else decipher(msg, keyword)

