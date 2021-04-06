
def sun_loungers(beach):
    count = 0
    beach = list(beach)
    if beach == ["0"]:
        return 1
    if beach[:2] == ["0", "0"]:
        beach[0] = "1"
        count += 1
    if beach[-2:] == ["0", "0"]:
        beach[-1] = "1"
        count += 1
    for i in range(1, len(beach) - 2):
        if beach[i - 1 : i + 2] == ["0", "0", "0"]:
            count += 1
            beach[i - 1 : i + 2] = ["0", "1", "0"]
    
    return count

