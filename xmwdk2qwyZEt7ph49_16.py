
def get_length(lst):
    return len(eval('[' + str(lst).replace('[', '').replace(']', '') +']'))

