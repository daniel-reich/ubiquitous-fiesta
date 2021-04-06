
def is_slidey(n):
    return all(abs(int(str(n)[i]) - int(str(n)[i - 1])) == 1
               for i in range(1, len(str(n)))) if n > 9 else True

