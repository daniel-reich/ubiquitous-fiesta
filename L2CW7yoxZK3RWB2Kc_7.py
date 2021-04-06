
def nico_cipher(message, key):
    # append spaces to ensure all columns are equal in length
    message += ' ' * ((len(key) - len(message) % len(key)) % len(key))
    # assign column order based on key value
    # order = [key.index(letter) for letter in sorted(key)] # elegant but can't handle repeats in key
    order = []
    # force repeated letters to point to different columns
    letter_pos = {letter: 0 for letter in key}
    for letter in sorted(key):
        pos = key.index(letter, letter_pos[letter])
        order.append(pos)
        letter_pos[letter] = pos + 1
    # split message into columns based on new order
    columns = [message[i::len(key)] for i in order]
    # unpack columns into string and return
    return ''.join(''.join(t) for t in zip(*columns))

