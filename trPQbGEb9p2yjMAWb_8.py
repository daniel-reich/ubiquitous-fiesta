
def every_some(*args):
    return (eval('all(x' + args[0] + ' for x in args[2:])')
            if args[1] == "everybody" else
            eval('any(x' + args[0] + ' for x in args[2:])'))

