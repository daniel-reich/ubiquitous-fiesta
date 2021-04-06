
def strong_password(password):
    dic = {
    "numbers" : set(list("0123456789")),
    "lower_case" : set(list("abcdefghijklmnopqrstuvwxyz")),
    "upper_case" : set(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")),
    "special_characters" : set(list("!@#$%^&*()-+"))
    }
    
    result = 4 - sum([1 for i in dic if len(dic.get(i) & set(password)) > 0])
    if result + len(password) < 6:
        return 6 - len(password)
    else:
        return result

