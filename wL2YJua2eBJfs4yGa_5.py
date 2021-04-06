
def babbage(n):
    target = str(n)
    number = 1
    notFound = True
    while notFound:
        check = str(number*number)
        if check == target:
            break
        if len(check) > len(target):
            if check[-len(target):] == target:
                break
        number+=1
    if n == 269696:
        if number == 99736:
            return "Babbage was correct!"
        else:
            return "Babbage was incorrect!"
    else:
        return number

