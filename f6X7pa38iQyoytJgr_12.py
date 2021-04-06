
def increasing_word_weights(sentence):
    lst_of_ord = [sum(ord(i) for i in s if i.isalpha()) for s in sentence.split()]
    return lst_of_ord == sorted(set(lst_of_ord))

