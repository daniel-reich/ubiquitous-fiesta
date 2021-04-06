
def bw_transform(text):
    bwm_list = [text]
    for _ in range(len(text)-1):
        new_entry = (bwm_list[-1][1:] + bwm_list[-1][0])
        bwm_list.append(new_entry)
    return "".join([word[-1] for word in sorted(bwm_list)])

