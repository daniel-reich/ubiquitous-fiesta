
def create_square(length):
    if length is None or length < 1:
        return ''
    elif length == 1:
        return '#'
    return '\n'.join('#{}#'.format(('#' if i == 0 or i == length - 1 else ' ')
                                   * (length - 2))
                     for i in range(length))

