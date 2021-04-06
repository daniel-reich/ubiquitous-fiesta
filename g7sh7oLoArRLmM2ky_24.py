
def baconify(msg, mask=""):
    enc_dict = {
"a":"uuuuu",
"b":"uuuul",
"c":"uuulu",
"d":"uuull",
"e":"uuluu",
"f":"uulul",
"g":"uullu",
"h":"uulll",
"i":"uluuu",
"j":"uluul",
"k":"ululu",
"l":"ulull",
"m":"ulluu",
"n":"ullul",
"o":"ulllu",
"p":"ullll",
"q":"luuuu",
"r":"luuul",
"s":"luulu",
"t":"luull",
"u":"luluu",
"v":"lulul",
"w":"lullu",
"x":"lulll",
"y":"lluuu",
"z":"lluul",
".":"llllu",
" ":"lllll"
}
​
    reverse_dict = {enc_dict[i]:i for i in enc_dict}
    
    if len(mask) == 0:
        new_msg = ""
        for i in range(len(msg)):
            if msg[i].isalpha():
                new_msg += msg[i]
        plain = ""
        length = len(new_msg)
        length = length - length%5
        for i in range(0, length,5):
            current = ""
            for j in range(5):
                if new_msg[i+j].isupper():
                    current = current + "u"
                else:
                    current = current + "l"
            
            plain += reverse_dict[current]
            
        return plain
    else:
        cipher_seq = ""
        for i in range(len(msg)):
            if msg[i].isalpha() or msg[i]=="." or msg[i]==" ":
                cipher_seq += enc_dict[msg[i].lower()]
        
        cipher_text = ""
        current_index = 0
        cipher_seq_len = len(cipher_seq)
        for j in range(len(mask)):
            if mask[j].isalpha():
                if current_index < cipher_seq_len:
                    if cipher_seq[current_index] == 'u':
                        cipher_text = cipher_text + mask[j].upper()
                    else:
                        cipher_text = cipher_text + mask[j].lower()
                    current_index = current_index + 1
                else:
                    cipher_text = cipher_text + mask[j]
            else:
                cipher_text = cipher_text + mask[j]
        return cipher_text

