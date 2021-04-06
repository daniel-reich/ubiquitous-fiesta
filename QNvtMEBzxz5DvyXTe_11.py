
def strong_password(password):
    def a(password):
        if any(i.isdigit() for i in password):
            return 0
        else:
            return 1    
    def b(password):
        if any(i.islower() for i in password):
            return 0
        else:
            return 1   
    def c(password):
        if any(i.isupper() for i in password):
            return 0
        else:
            return 1    
    def d(password):
        if any(i in "!@#$%^&*()-+" for i in password):
            return 0
        else:
            return 1    
    j=a(password)+b(password)+c(password)+d(password)
    if len (password)>=6 and j==0:
        return 0
    
    if len (password)>=6 and j!=0:
        return j
    
    else:
        return 6-len(password)

