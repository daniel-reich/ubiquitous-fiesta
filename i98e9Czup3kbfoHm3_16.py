
def text_to_number_binary(txt):
    conversion_table = {'zero': '0', 'one': '1'}
    # case insensitive, split by space
    words = txt.lower().split(' ')
    # remove unknown words
    words = [w for w in words if w in conversion_table]
    # truncate to multiple of 8
    length = len(words) // 8 * 8
    words = words[:length]
    # translate with the lookup table
    return ''.join(map(conversion_table.get, words))

