
def week_after(string):
    from calendar import monthrange
    date = string.split("/")
    days = monthrange(int(date[2]), int(date[1]))[1]
    date[0] = str(int(date[0]) + 7)
    if int(date[0]) > days:
        date[0], date[1] = str(int(date[0]) - days), str(int(date[1]) + 1)
    if int(date[1]) > 12:
        date[1], date[2] = "1", str(int(date[2])+1)
    for i in range(0,len(date),1):
        x = list(date[i])
        if len(x) == 1:
            x.insert(0,'0')
            date[i] = "".join(x)
    return "/".join(date)

