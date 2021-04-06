
def sun_loungers(beach):
    count = 0
    beach2 = '0'
    for i,j in enumerate(beach):
        foll = beach[i + 1] if i + 1 < len(beach) else '0' 
        prev = beach2[i]
        if j == '0':
            if prev == '0' and foll == '0':
                count += 1
                beach2 += '1'
            else:
                beach2 += j        
        else:
            beach2 += j
    return count

