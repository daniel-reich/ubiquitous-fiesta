
def sun_loungers(beach):
    count = 0
    beach_list = list(beach)
    if len(beach) == 1:
        if beach_list[0] == 1:
            return 0
        return 1
    for index, character in enumerate(beach_list):
        if character == '1':
            continue
        if index == 0:
            if beach_list[index + 1] == '0':
                count += 1
                beach_list[index] = '1'
        elif index == len(beach_list) - 1:
            if character == '0':
                if beach_list[index - 1] == '0':
                    count += 1
        elif beach_list[index - 1] == '0' and beach_list[index + 1] == '0':
            count += 1
            beach_list[index] = '1'
​
    return count

