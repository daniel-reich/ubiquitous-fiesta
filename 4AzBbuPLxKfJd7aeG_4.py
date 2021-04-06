
def encrypt(key, message):
    original_letter = []
    encrypted_letter = []
    for i in range(len(key)):
        if key[i].lower() not in original_letter:
            original_letter.append(key[i].lower())
            if i%2 == 0:
                encrypted_letter.append(key[i+1].lower())
            else:
                encrypted_letter.append(key[i-1].lower())
​
    encrypted_message = ""
    for i in range(len(message)):
        capital = message[i].isupper()
        if message[i].lower() in original_letter:
            for index, letter in enumerate(original_letter):
                if letter == message[i].lower():
                    if capital:
                        encrypted_message += encrypted_letter[index].upper()
                    else:
                        encrypted_message += encrypted_letter[index]
                    break
        else:
            encrypted_message += message[i]
            
    return(encrypted_message)

