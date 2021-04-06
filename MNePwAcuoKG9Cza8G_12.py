
def build_staircase(height, block):
    return [['_' if x>i else block for x in range(1, height+1)] for i in range(1,height+1)]

