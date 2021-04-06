
def letter_counter(lst, letter):
    a = 0
    for i in lst: 
        for x in i:
            if x == letter:
                a = a + 1
    return a

