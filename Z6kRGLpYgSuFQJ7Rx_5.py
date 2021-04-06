
def find_longest(sentence):
    result_list = sentence.split()
    max_word = ''
    current_word = ''
    for word in result_list:
        for i in range(len(word)):
            if not word[i].isalpha():
                current_word = word[:i]
                break
            else:
                current_word = word
​
        if len(current_word) >= len(max_word):
            max_word = current_word
        current_word = ''
​
    return max_word.lower()

