
def polybius(text):
    cipher_code="abcdefghiklmnopqrstuvwxyz"
    enc_dict = {cipher_code[i]:(int(i/5)+1, int(i%5)+1) for i in range(len(cipher_code))}
    dec_dict = {enc_dict[k]:k for k in enc_dict}
    result = ""
    if text[0].isalpha():
        for i in range(len(text)):
            current = text[i].lower()
            if current == 'j':
                current = 'i'
            if current.isalpha():
                x,y = enc_dict[current]
                result += str(x)+str(y)
            elif current == " ":
                result += text[i]
            
    else:
        count = 0
        for i in range(len(text)):
            if text[i].isdigit():
                if count%2 == 0:
                    x = int(text[i])
                    y =  int(text[i+1])
                    
                    result += dec_dict[(x,y)]
                count += 1
            else:
                result += text[i]
    
    return result

