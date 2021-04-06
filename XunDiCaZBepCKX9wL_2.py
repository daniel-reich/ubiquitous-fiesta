
def secret_word(string, length):
    triplets = [(ord(t[0]) + ord(t[1]) + ord(t[2]) - 3 * ord('a'), t[1]) for t in zip(string, string[1:], string[2:])]
    for ix, tri in enumerate(triplets):
        for j in range(ix+1, len(triplets)):
            secret = tri[1]
            if triplets[j][0] > triplets[ix][0]:
                d, prev = triplets[j][0] - triplets[ix][0], triplets[j][0]
                secret += triplets[j][1]
                for k in range(j+1, len(triplets)):
                    if triplets[k][0] - prev == d:
                        secret += triplets[k][1]
                        prev = triplets[k][0]
            if len(secret) == length:
                return secret
    return None

