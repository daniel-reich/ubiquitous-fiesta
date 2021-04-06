
def get_name(address):
    name_with_numbers = []
    doContinue = False
    for char in address:
        if doContinue:
            continue
        elif char == '@':
            doContinue = True
        else:
            name_with_numbers.append(char)
        complete_name = ''
    for item in name_with_numbers:
        if item.isalpha():
            complete_name += item
    return complete_name

