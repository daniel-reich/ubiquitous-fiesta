
def is_it_inside(folders: dict, subfolder: int, targetfolder: int):
    if subfolder == targetfolder:
        return True
    if targetfolder not in folders:
        return False
    if subfolder in folders[targetfolder]: # list
        return True
​
    else:
        l = []
        for f in folders[targetfolder]:
            if f in folders: # it has a list
                for k in folders[f]:
                    if k in folders:
                        l.extend(folders[k])
                    else:
                        l.append(k)
        return subfolder in l

