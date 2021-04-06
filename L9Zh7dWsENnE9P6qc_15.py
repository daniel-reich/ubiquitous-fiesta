
def josephus(people):
    if people == 1:
        return 1
    if people%2 == 0:
        return 2 * josephus(people / 2) - 1
    if people%2 == 1:
        return 2 * josephus((people - 1) / 2) + 1

