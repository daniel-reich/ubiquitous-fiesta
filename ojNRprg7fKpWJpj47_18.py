
def shift_sentence(txt):
    first_letter = [a[0] for a in txt.split(' ')]
    first_letter_new_index =  list(first_letter[-1]) + first_letter[0:len(first_letter)-1]
    other_letters = [a[1:] for a in txt.split(' ')]
    return ' '.join([''.join(a) for a in list(zip(first_letter_new_index, other_letters))])

