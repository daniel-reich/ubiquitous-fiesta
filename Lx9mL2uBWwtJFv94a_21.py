
def checker_board(n, *element):
​
    if element[0] == element[1]:
        return "invalid"
​
    current_index = 0
    result = []
​
    for row in range(n):
        result.append([])
        for column in range(n):
            result[row].append(element[current_index])
​
            if column == n - 1 and n % 2 == 0:
                pass
            else:
                current_index = abs(current_index - 1)
​
    return result

