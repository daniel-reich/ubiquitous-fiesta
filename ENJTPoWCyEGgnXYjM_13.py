
def percent_filled(array):
    free_blocks, filled_blocks = 0,0
    for i in array:
        for e in range(0,len(i),1):
            if i[e] != "#":
                free_blocks += 1
            if i[e] != "#" and i[e] != " ":
                filled_blocks += 1
    return "{}%".format(int((int(filled_blocks)/int(free_blocks))*100))

