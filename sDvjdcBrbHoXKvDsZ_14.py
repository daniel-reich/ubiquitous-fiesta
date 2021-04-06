
def anagram(name, words):
    name_lst = [char.lower() for char in name if char != ' ']
    words_lst = [letter.lower() for word in words for letter in word]
    return len(words_lst) == len(name_lst) and words_lst.sort() == name_lst.sort()

