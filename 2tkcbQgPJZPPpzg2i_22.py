
def sum_of_holes(n):
    scores = {0: 1, 1: 0, 2: 0, 3: 0, 4: 1, 5: 0, 6: 1, 7: 0, 8: 2, 9: 1}
    total = 0
    for i in range(1, n+1):
        if len(str(i)) > 1:
            list_of_n = list(str(i))
            for j in list_of_n:
                if int(j) in scores.keys():
                    total += scores[int(j)]
        else:
            total += scores[int(i)]
    return total

