
def babbage(ends):
    cycle = {0: {0: 10}, 1: {1: 8, 9: 2}, 4: {2: 6, 8: 4}, 5: {5: 10}, 6: {4: 2, 6:8}, 9: {3: 4, 7: 6}}[ends%10]
    trial, endstr = {0: 10, 1: 1, 4: 2, 5: 5, 6: 4, 9: 3}[ends%10], str(ends)
    while True:
        if str(trial**2).endswith(endstr):
            return trial if ends != 269696 else "Babbage was {}correct!".format('' if trial == 99736 else 'in') 
        trial += cycle[trial%10]

