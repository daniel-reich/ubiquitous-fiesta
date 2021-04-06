
def extend_vowels(word, num):
    return "invalid" if num<0 or type(num)==float else ''.join([i if i not in 'aeiouAEIOU' else i + i*num for i in word])

