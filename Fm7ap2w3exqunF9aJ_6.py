
def count_lone_ones(n):
    string = '$' + str(n) + '$'
    return sum(
        i != '1' and j == '1' and k != '1'
        for i, j, k in zip(string, string[1:], string[2:])
    )

