
def count(deck):
    result = 0
    for i in deck:
        if str(i) in '2,3,4,5,6': result += 1
        elif str(i) in '10,J,Q,K,A': result -= 1
    return result

