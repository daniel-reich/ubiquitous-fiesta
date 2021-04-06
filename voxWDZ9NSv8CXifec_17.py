
def lemonade(bills):
    change = []
    for i in bills:
        try:
            if i == 5:
                change.append(5)
            elif i == 10:
                change.append(10)
                change.remove(5)
            else:
                change.append(20)
                change.remove(10)
                change.remove(5)
        except ValueError:
            return False
    return True

