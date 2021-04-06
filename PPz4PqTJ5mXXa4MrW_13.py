
def ulam(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    if n == 4:
        return 4
​
    array = [1, 2, 3, 4]
    evaluate = []
    i = 0
    h = 0
​
    if n > 4:
        while i < len(array) - 1:
            while h < len(array) - 1 - i:
                array[i] += array[h]
                evaluate.append(array[i])
                if len(array) == n:
                    break
            h += 1
        i += 1
​
        evaluate.sort()
        for y in range(len(evaluate)):
            if evaluate[y] not in array and evaluate.count(evaluate[y]) == 1:
                array.append(evaluate[y])
​
        return array[len(array) - 1]

