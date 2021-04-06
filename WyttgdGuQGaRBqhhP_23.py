
def is_palindrome(st):
    return st == st[::-1]
​
​
​
​
def min_palindrome_steps(n_word):
    x = 0
    addition = ""
    while not is_palindrome(n_word + addition):
        addition = n_word[x] + addition
        print(n_word+addition)
        x += 1
    return x

