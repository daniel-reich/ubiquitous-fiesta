
from collections import Counter
​
def sequenceCheck(n, List):
    List.sort()
    counter = 1
    i = 0
    while i <= 3:
        if List[i + 1] == List[i] + 1:
            counter += 1
        i += 1
    if counter >= n:
        return True
    else:
        return False    
    
​
def most_frequent(List): 
    return List.count(max(set(List), key = List.count))
​
def yahtzee_score_calc(lst):
    result = 0
    i = 0
    while i < 13:
        if i < 6:
            for j in range(5):
                if lst[i][j] == i + 1:
                    result += i + 1
            if result >= 63:
                result += 35
        elif i == 6:
            if most_frequent(lst[i]) >= 3:
                result += sum(lst[i])
            print("7 " + str(result))
        elif i == 7:
            if most_frequent(lst[i]) >= 4:
                result += sum(lst[i])
            print("8 " + str(result))
        elif i == 8:
            if most_frequent(lst[i]) == 3 and len(Counter(lst[i]).keys()) == 2:
                result += 25
            print("9 " + str(result))
        elif i == 9:
            if sequenceCheck(4, lst[i]):
                result += 30
            print("10 " + str(result))
        elif i == 10:
            if sequenceCheck(5, lst[i]):
                result += 40
            print("11 " + str(result))
        elif i == 11:
            if lst[i].count(lst[i][0]) == len(lst[i]):
                result += 50
            print("12 " + str(result))
        elif i == 12:
            result += sum(lst[i])
            print("13 " + str(result))
        else:
            print("error")
        i += 1
    return result

