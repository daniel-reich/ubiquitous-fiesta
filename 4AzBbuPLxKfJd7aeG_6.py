
def encrypt(ky,message):
    message = list(message)
    k = 0
    while k in range(len(message)):
        for it in ([al for n in range(0, len(ky), 2) for al in (ky[n:n + 2], ky[n:n + 2][::-1])]):
            if it.startswith(message[k]):
                message[k] = it[1]
                break
        k+=1
    return ("".join(message))

