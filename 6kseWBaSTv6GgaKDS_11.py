
def next_letters(s):
    if not s:
        return 'A'
    else:
        if not s[-1]=='Z':
            return s[0:-1]+chr(ord(s[-1])+1)
        else:
            i=len(s)
            while(i>0):
                if s[i-1]=='Z':
                    i=i-1
                else:
                    break
            if i==0:
                return 'A'*(len(s)+1)
            else:
                return s[0:i-1]+chr(ord(s[i-1])+1)+'A'*(len(s)-i)

