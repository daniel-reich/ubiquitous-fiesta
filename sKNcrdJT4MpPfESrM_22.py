
def remove_virus(files):
    temp = files[10:].split(', ')
    myans = []
    for i in temp:
        if 'virus' in i:
            if i == 'notvirus.exe':
                myans.append(i)
            if i == 'antivirus.exe':
                myans.append(i)
​
        elif 'malware' in i:
            pass
​
        else:
            myans.append(i)
​
    if len(myans) == 0:
        return 'PC Files: Empty'
    else:
        return 'PC Files: ' + ', '.join(myans)

