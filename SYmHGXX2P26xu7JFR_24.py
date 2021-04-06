
def number_groups(group1, group2, group3):
    arr = []
    group1 = [str(i) for i in group1]
    group2 = [str(i) for i in group2]
    group3 = [str(i) for i in group3]
    for i in range(len(group1)):
        if group1[i] in group2 or group1[i] in group3:
            arr.append(group1[i])
        if group2[i] in group3:
            arr.append(group2[i])
    answer = []
    for i in arr:
        if i not in answer:
            answer.append(i)
    answer = [int(i) for i in answer]
    answer.sort()
​
    return answer

