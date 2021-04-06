
def strong_password(pw):
    if len(pw) < 6:
        return 6 - len(pw) 
    else:    
        return [any(x.isdigit() for x in pw),
            any(x in "abcdefghijklmnopqrstuvwxyz" for x in pw),
            any(x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for x in pw),
            any(x in "!@#$%^&*()-+" for x in pw)].count(False)

