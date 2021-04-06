
def transform_matrix(lst):
    columns = list(map(list,zip(*lst)))
    ans = [i.copy() for i in lst]
    for row in range(len(ans)):
        for i in range(len(ans[row])):
            ans[row][i] = (sum(lst[row])-ans[row][i]) + (sum(columns[i]) - columns[i][row])  
    return ans

