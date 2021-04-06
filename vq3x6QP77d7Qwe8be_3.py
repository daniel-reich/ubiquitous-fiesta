
def is_all_odd(sub):
    for i in range(len(sub)):
        for j in range(len(sub[0])):
            if sub[i][j]%2==0:
                return False
    return True
def odd_square_patch(lst):
    width, height, squares = len(lst[0]), len(lst), [0]
    for i in range(height):
        for j in range(width):
            if lst[i][j]%2 == 1:
                squares.append(1)
                for k in range(1, min([height-i, width-j])+1):
                    arr = [lst[l][j: j+k] for l in range(i, i+k)]
                    if is_all_odd(arr):
                        squares.append(k)
    return max(squares)

