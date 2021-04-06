
def babbage(n):
    r = next(i for i in range(int(n**.5), n+1) if str(i**2).endswith(str(n)))
    return r if n!=269696 else "Babbage was {}correct!".format("in" if r!=99736 else "")

