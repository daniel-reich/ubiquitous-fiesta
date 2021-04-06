
def shift_letters(txt, n):
    location = [i for i in range(len(txt)) if txt[i] == " "]
    new_txt = txt.replace(" ", "", txt.count(" "))
    n = n % len(new_txt)
    final_txt = new_txt[-n:] + new_txt[:-n]
    for i in location:
        final_txt = final_txt[:i] + " " +final_txt[i:]
    return final_txt

