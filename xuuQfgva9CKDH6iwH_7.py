
def simulate_grass(g, x, y):
    if g[x][y] == "x":
        return g
    initial_result = []
    for i in range(len(g)):
        initial_result.append(list(g[i]))
    initial_result[x][y] = "+"
    for i in range(len(initial_result)):
        for j in range(len(initial_result[0])):
            if initial_result[i][j] == "+":
                if i > 0:
                    for k in range(i, -1, -1):
                        if initial_result[k][j] == "x":
                            break
                        else:
                            initial_result[k][j] = "+"
                if i < len(initial_result) - 1:
                    for k in range(i + 1, len(initial_result)):
                        if initial_result[k][j] == "x":
                            break
                        else:
                            initial_result[k][j] = "+"
                if j > 0:
                    for k in range(j, -1, -1):
                        if initial_result[i][k] == "x":
                            break
                        else:
                            initial_result[i][k] = "+"
                if j < len(initial_result[0]) - 1:
                    for k in range(j + 1, len(initial_result[0])):
                        if initial_result[i][k] == "x":
                            break
                        else:
                            initial_result[i][k] = "+"
            if initial_result[i][j] == "o":
                if i + 1 < len(initial_result) and initial_result[i+1][j] == "+":
                    initial_result[i][j] = "+"
                elif i > 0 and initial_result[i-1][j] == "+":
                    initial_result[i][j] = "+"
                elif j > 0 and initial_result[i][j-1] == "+":
                    initial_result[i][j] = "+"
                elif j < len(initial_result[0]) - 1 and initial_result[i][j-1] == "+":
                    initial_result[i][j+1] = "+"
    result = []
    for i in range(len(initial_result)):
        result.append("".join(initial_result[i]))
    if result == g:
        return result
    return simulate_grass(result, x, y)

