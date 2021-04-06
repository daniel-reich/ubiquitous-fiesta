
def caesar_cipher(s, k):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet2 = alphabet.upper()
    output = ""
    for i in s:
        if i in alphabet:
            output += (alphabet[(alphabet.index(i)+k)%26])
        elif i in alphabet2:
            output += (alphabet2[(alphabet2.index(i)+k)%26])
        else:
            output += i
        
    return output

