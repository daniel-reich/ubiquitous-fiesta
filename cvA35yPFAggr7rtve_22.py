
def last_ancestor(folders, x, y):
    def find_branch(a):
        res = [a]
        while res[-1] != 'root':
            found = False
            for key, val in folders.items():
                if a in val:
                    res.append(key)
                    a = key
                    found = True
            if not found:
                res.append('root')
        return res
    branch_x = find_branch(x)
    branch_y = find_branch(y)
    for folder in branch_x:
        if folder in branch_y:
            return folder
    return 'root'

