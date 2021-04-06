
def tree(n):
    if n == 0:
         return []
    width = (2 * n) - 1
    output = []
    branch = '#'
    blankwidth = (width - len(branch)) // 2
    for i in range(n):
         output.append((' ' * blankwidth) + branch + (' ' * blankwidth))
         branch += '##'
         blankwidth = (width - len(branch)) // 2
    return output

