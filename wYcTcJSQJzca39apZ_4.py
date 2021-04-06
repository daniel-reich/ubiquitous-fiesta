
def truncate(txt, length):
    words = txt.split(' ')
    cur_len = sum(map(len, words)) + len(words) - 1
    while cur_len > length:
        popped = words.pop()
        cur_len -= 1 + len(popped)
    return ' '.join(words)

