
def remove_virus(files):
    lst = files[files.index(":")+1::].split(", ")
    result = list()
    for file in lst:
        if "virus" in file and "antivirus" not in file and "notvirus" not in file:
            pass
        elif "malware" in file:
            pass
        else:
            result.append(file)
    return "PC Files:"+", ".join(result) if result else "PC Files: Empty"

