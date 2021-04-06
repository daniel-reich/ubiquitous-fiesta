
def caesar_cipher(text, key):
    RESULT = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    print(len(alphabet))
    
    for elem in list(str(text)):
        if elem in list(alphabet):
            POSITION = alphabet.find(elem)
            key2 = alphabet.find(elem) + key
            if key2 > 25:
                key2 = key2 - 26
                print(key2, RESULT, alphabet.find(elem) + key )
            RESULT.append(list(alphabet)[key2])
        else:
            RESULT.append(' ')
    
    
    print(''.join(RESULT))
    return ''.join(RESULT)
    
caesar_cipher("iwxh xh p rwxetg", 11)

