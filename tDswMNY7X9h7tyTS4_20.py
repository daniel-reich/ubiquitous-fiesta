
pascal = [[1]]
line = [1, 1]
for _ in range(2, 50):
    new_line = [1]
    for i in range(1, len(line)):
        new_line.append(line[i - 1] + line[i])
    new_line.append(1)
    pascal.append(line[:])
    line = new_line[:]
​
def pascals_triangle(n):
    ans = []
    for i in range(n):
        ans += pascal[i]
    return ans

