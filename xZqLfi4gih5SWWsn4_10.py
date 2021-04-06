
def license_plate(code, group, ans=""):
    if code == "":
        return ans[::-1]
    if ans == "":
        code = code.upper().replace('-', '')[::-1]
        return license_plate(code[1:], group, code[0])
    if len(ans) < group:
        return license_plate(code[1:], group, ans + code[0])
    elif len(ans) == group:
        return license_plate(code[1:], group, ans + "-" + code[0])
    else:
        if len(ans.split('-')[-1]) < group:
            return license_plate(code[1:], group, ans + code[0])
        else:
            return license_plate(code[1:], group, ans + "-" + code[0])

