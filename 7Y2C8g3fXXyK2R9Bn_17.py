
def keyword_cipher(key, message):
    alphabet = ''.join( [chr(i  + 97)  
                for i in range (0,26)  ])
    code  = (''.join([k for ix,k in enumerate(key) 
                    if ix == key.index(k)])  
        +   ''.join([chr(i  + 97)  
                for i in range (0,26) 
                if chr(i + 97) not in key]  )
                )
    return ''.join ([ code[alphabet.index(s)] if s in code else s 
            for s in message])

