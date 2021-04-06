
def title_to_number(column_title):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    column_number = 0
    for index, character in enumerate(column_title[::-1]):
        position = alphabet.find(character) + 1
        column_number += position * (26 ** index)
    return column_number

