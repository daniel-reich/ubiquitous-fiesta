
def calculate_score(array):
    Abigail = 0
    Benson = 0
    for i in range(len(array)):
        if (array[i][0] == "R" and array[i][1] == "S") :Abigail += 1
        if (array[i][0] == "S" and array[i][1] == "P") :Abigail += 1
        if (array[i][0] == "P" and array[i][1] == "R") :Abigail += 1
        if (array[i][0] == "S" and array[i][1] == "R") :Benson += 1
        if (array[i][0] == "P" and array[i][1] == "S") :Benson += 1
        if (array[i][0] == "R" and array[i][1] == "P") :Benson += 1
    return 'Tie' if Abigail==Benson else 'Abigail' if Abigail>Benson else 'Benson'

