
def sun_loungers(beach):
    result = 0
    beach = list(beach)
    for i in range(len(beach)):
        prev = beach[i-1:i]
        next = beach[i+1:i+2]
        if beach[i] == '0':
            if prev != ['1'] and next != ['1']:
                beach[i] = '1'
                result += 1
    return(result)

