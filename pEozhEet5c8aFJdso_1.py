
def all_about_strings(txt):
    count = 0
    count1 = 0
    all_about = []
    all_about.append(len(txt))
    all_about.append(txt[0])
    all_about.append(txt[len(txt)-1])
    number = len(txt) % 2
    if number == 0:
        a = len(txt) / 2
        all_about.append(txt[round(a)-1] + txt[round(a)])
    elif number == 1:
        b = len(txt) / 2
        all_about.append(txt[int(b)])
    for item in txt:
        count1 += 1
        if txt[1] == item:
            count += 1
            if count > 1:
                all_about.append('@ index ' + str(count1-1) )
        elif count == 1 and count1 == len(txt):
            all_about.append('not found')
    return all_about
print(all_about_strings('Seadaaa'))

