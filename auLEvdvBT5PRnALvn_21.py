
def mirror_cipher(*args):
    message, a, b = args[0], [], []
    m = list(message.lower())
    abc = list(("ABCDEFGHIJKLMNOPQRSTUVWXYZ").lower())
    if len(args)==2:
        key=args[1]
        k = list(key.lower())
        for i in m:
            if i in k:a.append(k[-k.index(i)-1])
            else: a.append(i)
        return "".join(a)   
    else:
        for i in m:
            if i == " ": b.append(" ")
            else:b.append(abc[-abc.index(i)-1])
        return "".join(b)

