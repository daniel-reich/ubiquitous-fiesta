
def possible_palindrome(txt):
    c = [0] * 256 
    for i in range( 0, len(txt)) : 
        c[ord(txt[i])] = c[ord(txt[i])] + 1
    odd = 0
    for i in range(0, 256) : 
        if (c[i] & 1) : 
            odd += 1
  
        if (odd > 1) : 
            return False
              
  
    return True

