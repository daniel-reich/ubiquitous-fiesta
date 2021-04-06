
def avg_note(students):
    ans = []
    for din in students:
        dout = {}
        dout['name'] = din['name']
        x = din['notes']
        if x:
            avg = round(sum(x) / len(x))
        else:
            avg  = 0
        dout['avgNote'] = avg
        ans.append(dout)
    return ans

