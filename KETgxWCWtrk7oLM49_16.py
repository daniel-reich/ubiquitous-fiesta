
def tournament_scores(list1):
    dict1 = {}
    for game in list1:
        list2 = game.split()
        if list2[0] not in dict1.keys():
            dict1[list2[0]] = [0, int(list2[1]), int(list2[3])]
        else:
            dict1[list2[0]][1] += int(list2[1])
            dict1[list2[0]][2] += int(list2[3])
        if list2[4] not in dict1.keys():
            dict1[list2[4]] = [0, int(list2[3]), int(list2[1])]
        else:
            dict1[list2[4]][1] += int(list2[3])
            dict1[list2[4]][2] += int(list2[1])
​
        if list2[1] > list2[3]:
            dict1[list2[0]][0] += 3
        elif list2[1] < list2[3]:
            dict1[list2[4]][0] += 3
        else:
            dict1[list2[0]][0] += 1
            dict1[list2[4]][0] += 1
    print(dict1)
    list3 = []
    keys_list = [x for x in dict1.keys()]
    while True:
        if keys_list:
            highest = keys_list[0]
            for key in keys_list:
                if dict1[key][0] > dict1[highest][0]:
                    highest = key
                elif dict1[key][0] == dict1[highest][0]:
                    if dict1[key][1] > dict1[highest][1]:
                        highest = key
                    elif dict1[key][1] == dict1[highest][1]:
                        if dict1[key][1] - dict1[key][2] > dict1[highest][1] - dict1[highest][2]:
                            highest = key
​
            list3.append([highest, dict1[highest][0], dict1[highest][1], dict1[highest][1] - dict1[highest][2]])
            keys_list.remove(highest)
        else:
            break
    return list3

