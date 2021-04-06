
def can_see_stage(rows):
    temp_list = []
    for i in range(len(rows[0])):
        temp_list = []
        for row in rows:
            temp_list.append(row[i])
            for j in range(0, len(temp_list)-1):
                if temp_list[j] < temp_list[j+1]:
                    pass
                else:
                    return False
                    break
    return True

