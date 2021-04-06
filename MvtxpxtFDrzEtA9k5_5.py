
def palindrome_descendant(num):
    def is_palindrome(num):
        num = str(num)
        if num=='':
            return True
        if num[0]!=num[-1]:
            return False
        elif num[0]==num[-1]:
            return is_palindrome(num[1:-1])
    
    if len(str(num))==1:
        return False
    if is_palindrome(num):
        return True
    else:
        s = str(num)
        try:
            descendant = int(''.join([str(int(s[i])+int(s[i+1])) for i in range(0,len(s),2)]))
            return palindrome_descendant(descendant)
        except:
            return False

