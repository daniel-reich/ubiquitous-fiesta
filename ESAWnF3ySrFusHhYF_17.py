
def edit_words(lst):
    return [
    ''.join(add_hyphen(words)[::-1].upper()) 
    for words in lst
  ]
​
def add_hyphen(string):
    half = len(string) // 2
    return string[:half] + '-' + string[half:]

