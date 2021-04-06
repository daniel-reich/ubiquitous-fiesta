
def vowels(string):
    input = str(string)
    count = 0
    vows = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(input)):
        if input[i] in vows:
            count += 1
    return count

