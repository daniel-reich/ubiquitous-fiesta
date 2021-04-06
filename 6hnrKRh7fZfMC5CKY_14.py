
def look_and_say(n):
    
    if len(str(n))%2!=0:
        return 'invalid'
    
    else:
        pairs_lst  = [str(n)[i:i+2] for i in range(0, len(str(n)), 2)]
​
    
    return int(''.join([int(pair[0])*pair[1] for pair in pairs_lst]))

