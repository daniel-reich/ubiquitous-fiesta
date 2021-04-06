
def drange(*args):
    if len(args) == 1:
        return drange(0, args[0], 1)
    elif len(args) == 2:
        return drange(args[0], args[1], 1)
    else:
        dp = max([len(str(i)[str(i).find('.'):])-1 for i in args])
        i = round(args[0], dp)
        tup = [i]
        while i + args[2] < args[1]:
            i = round(i + args[2],dp)
            tup.append(i)
    return tuple(tup)

