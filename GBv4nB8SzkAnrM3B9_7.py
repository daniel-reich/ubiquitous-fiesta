
def letter_counter(lst, letter):
    count = 0
    for row in lst:
        for character in row:
            if character == letter:
                count+=1
    return count

