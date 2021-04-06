
def ping_pong(lst, win):
    result = []
    for i in range(len(lst)):
        result.extend([lst[i], "Pong!"])
    if win and result[-1] != "Pong!":
        result.append("Pong!")
    elif not win and result[-1] != "Ping!":
        result = result[:-1]
    return result

