
def every_some(expr, option, *args) -> bool:
    L = [str(i) + ' ' + expr for i in args]
    if option == "everybody":
        return all(eval(i) for i in L)
    else:
        return any(eval(i) for i in L)

