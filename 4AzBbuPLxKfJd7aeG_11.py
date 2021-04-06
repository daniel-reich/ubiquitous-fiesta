
def encrypt(key, message):
    keys = [key[i:i + 2] for i in range(0, len(key), 2)]
    output = ''
    for i in message:
        found = 0
        for j in keys:
            if i in j:
                output += j.replace(i, '')
                found = 1
                break
        if not found:
            output += i
    return output

