
def pad(message):
    a =((140-len(message)-1)%2)
    add = 'lo' * ((140-len(message))//2) + ('l' * (len(message) % 2))
    return (message +' '*a + add[:len(add)-a]).strip()

