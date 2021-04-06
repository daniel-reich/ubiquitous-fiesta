
def remove_virus(files):
    pcfiles = "PC Files:"
    viruses = ["virus", "malware"]
    notviruses = ["antivirus", "notvirus"]
    
    files = files.split()
    files.pop(0); files.pop(0)
    count = 0
    for idx, file in enumerate(files):
        if notviruses[0] in file or notviruses[1] in file:
            count += 1
            pcfiles += " "+file
        if viruses[0] in file or viruses[1] in file:
            continue
        else:
            count += 1
            pcfiles += " "+file
    if pcfiles[-1] == ",":
        pcfiles = pcfiles[:-1]
    if count == 0:
        pcfiles += " Empty"
    return pcfiles

