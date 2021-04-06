
def num_in_str(lst):
    output = []
    for i in range(len(lst)):
        for letters in lst[i]:
            if letters.isnumeric() == True:
               output.append(lst[i])
               break
    return output

