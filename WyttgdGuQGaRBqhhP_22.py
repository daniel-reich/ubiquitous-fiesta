
def min_palindrome_steps(txt):
    word, let = txt, 0
    while word != word[::-1]:
        word, let = txt, let+1
        word = word+word[0:let][::-1]
    return let

