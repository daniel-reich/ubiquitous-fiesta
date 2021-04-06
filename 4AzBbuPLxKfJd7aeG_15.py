
def encrypt(key, message):
    return ''.join(  [ lett if lett not in key 
        else  key[key.index(lett) - 1] 
              if (key.index(lett) + 1) %2 ==0 
        else  key[key.index(lett) + 1] 
        for lett in message]
         )

