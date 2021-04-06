
def pad(message):
    p = 'ol'*70
    t = len(message)
    if t == 140:
        return message
    elif not t % 2:
        return message+" "+ p[t+1:]
    else:
        return message+p[t:]

