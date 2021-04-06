
def time_to_eat(current_time):
    pm = {
        "1": "13",
        "2": "14",
        "3": "15",
        "4": "16",
        "5": "17",
        "6": "18",
        "7": "19",
        "8": "20",
        "9": "21",
        "10": "22",
        "11": "23",
        "12": "0"
    }
    eat_time = [7, 12, 19]
​
    inp = current_time.split()
    inp[0] = inp[0].split(':')
    time = inp[0]
​
    time[0] = pm[str(inp[0][0])] if inp[1] == 'p.m.' and int(inp[0][0]) <= 12 else inp[0][0]
    time[0] = int(time[0])
    time[1] = int(time[1])
​
    diff = [24, 0 if time[1] == 0 else 60 - time[1]]
​
    if time[1] != 0:
        time[0] = time[0] + 1
​
    if time[0] == 12 or time[0] == 24 and inp[1] == 'p.m.':
        time[0] = 0
​
    if time[0] > 19:
        diff[0] = 7 + (24 - time[0])
    else:
        for i in eat_time:
            tmp = i - time[0]
            diff[0] = tmp if 0 <= tmp < diff[0] else diff[0]
    return diff

