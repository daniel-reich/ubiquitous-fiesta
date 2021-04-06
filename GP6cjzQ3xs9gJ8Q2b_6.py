
def is_polydivisible(number):
    if len(str(number)) < 4:
        return True
    else:
        str_number = str(number)
        for i in range(2,len(str_number)+1):
            substring = str_number[0:i]
            if int(substring) % len(substring) == 0:
                continue
            else:
                return False
        return True

