
from operator import itemgetter
def update_table(str0, listA, listB, listC, listD):
    if str0[2] > str0[6]:  # left won
        # winner
        if str0[0] == "A":
            listA[1] += 3
            listA[2] += int(str0[2])
            listA[3] = listA[3] + int(str0[2]) - int(str0[6])
​
        if str0[0] == "B":
            listB[1] += 3
            listB[2] += int(str0[2])
            listB[3] = listB[3] + int(str0[2]) - int(str0[6])
​
        if str0[0] == "C":
            listC[1] += 3
            listC[2] += int(str0[2])
            listC[3] = listC[3] + int(str0[2]) - int(str0[6])
​
        if str0[0] == "D":
            listD[1] += 3
            listD[2] += int(str0[2])
            listD[3] = listD[3] + int(str0[2]) - int(str0[6])
        # looser:
        if str0[8] == "A":
            listA[2] += int(str0[6])
            listA[3] = listA[3] + int(str0[6]) - int(str0[2])
​
        if str0[8] == "B":
            listB[2] += int(str0[6])
            listB[3] = listB[3] + int(str0[6]) - int(str0[2])
​
        if str0[8] == "C":
            listC[2] += int(str0[6])
            listC[3] = listC[3] + int(str0[6]) - int(str0[2])
​
        if str0[8] == "D":
            listD[2] += int(str0[6])
            listD[3] = listD[3] + int(str0[6]) - int(str0[2])
​
    elif str0[2] < str0[6]:  # right won
        # winner
        if str0[8] == "A":
            listA[1] += 3
            listA[2] += int(str0[6])
            listA[3] = listA[3] + int(str0[6]) - int(str0[2])
​
        if str0[8] == "B":
            listB[1] += 3
            listB[2] += int(str0[6])
            listB[3] = listB[3] + int(str0[6]) - int(str0[2])
​
        if str0[8] == "C":
            listC[1] += 3
            listC[2] += int(str0[6])
            listC[3] = listC[3] + int(str0[6]) - int(str0[2])
​
        if str0[8] == "D":
            listD[1] += 3
            listD[2] += int(str0[6])
            listD[3] = listD[3] + int(str0[6]) - int(str0[2])
        # looser:
        if str0[0] == "A":
            listA[2] += int(str0[2])
            listA[3] = listA[3] + int(str0[2]) - int(str0[6])
​
        if str0[0] == "B":
            listB[2] += int(str0[2])
            listB[3] = listB[3] + int(str0[2]) - int(str0[6])
​
        if str0[0] == "C":
            listC[2] += int(str0[2])
            listC[3] = listC[3] + int(str0[2]) - int(str0[6])
​
        if str0[0] == "D":
            listD[2] += int(str0[2])
            listD[3] = listD[3] + int(str0[2]) - int(str0[6])
    else:  # tie
        # left side
        if str0[8] == "A":
            listA[1] += 1
            listA[2] += int(str0[6])
            listA[3] = listA[3] + int(str0[6]) - int(str0[2])
​
        if str0[8] == "B":
            listB[1] += 1
            listB[2] += int(str0[6])
            listB[3] = listB[3] + int(str0[6]) - int(str0[2])
​
        if str0[8] == "C":
            listC[1] += 1
            listC[2] += int(str0[6])
            listC[3] = listC[3] + int(str0[6]) - int(str0[2])
​
        if str0[8] == "D":
            listD[1] += 1
            listD[2] += int(str0[6])
            listD[3] = listD[3] + int(str0[6]) - int(str0[2])
        # looser:
        if str0[0] == "A":
            listA[1] += 1
            listA[2] += int(str0[2])
            listA[3] = listA[3] + int(str0[2]) - int(str0[6])
​
        if str0[0] == "B":
            listB[1] += 1
            listB[2] += int(str0[2])
            listB[3] = listB[3] + int(str0[2]) - int(str0[6])
​
        if str0[0] == "C":
            listC[1] += 1
            listC[2] += int(str0[2])
            listC[3] = listC[3] + int(str0[2]) - int(str0[6])
​
        if str0[0] == "D":
            listD[1] += 1
            listD[2] += int(str0[2])
            listD[3] = listD[3] + int(str0[2]) - int(str0[6])
​
def tournament_scores(lst): # 2,6, stri length = 9
    str1 = str(lst[0])
    str2 = str(lst[1])
    str3 = str(lst[2])
    str4 = str(lst[3])
    str5 = str(lst[4])
    str6 = str(lst[5])
    list_a = ["A", 0 , 0 ,0]
    list_b = ["B", 0 , 0 ,0]
    list_c = ["C", 0 , 0 ,0]
    list_d = ["D", 0 , 0 ,0]
    update_table(str1, list_a,list_b, list_c,list_d)
    update_table(str2, list_a, list_b, list_c, list_d)
    update_table(str3, list_a, list_b, list_c, list_d)
    update_table(str4, list_a, list_b, list_c, list_d)
    update_table(str5, list_a, list_b, list_c, list_d)
    update_table(str6, list_a, list_b, list_c, list_d)
​
    res = [list_a, list_b, list_c, list_d]
    res_sort1 = sorted(res, key = itemgetter(1,3))
    res_sort1.reverse()
​
​
    return res_sort1

