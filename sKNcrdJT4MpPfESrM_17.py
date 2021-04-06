
def remove_virus(lst):
    lst = lst[10:]
    lst = lst.split(", ")
    newlst = []
    for i in lst:
        var = i.split(".")
        vartest = var[0]
        if "virus" in vartest or "malware" in vartest:
            if "antivirus" in vartest or "notvirus" in vartest:
                newlst.append(var[0] + "." + var[1])
        else:
            newlst.append(i)
    if len(newlst) != 0:
        lstresult = "PC Files:"
        for i in newlst:
            lstresult = lstresult + " " + i + ","
        lstresult = lstresult[:-1]
    else:
        lstresult = "PC Files: Empty"
    return lstresult;

