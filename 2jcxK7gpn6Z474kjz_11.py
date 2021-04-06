
def security(txt):
    if "T" not in txt or "$" not in txt or ("G" not in txt and "$" not in txt):
        return "Safe"
    i_money = txt.index("$")
    if "T" in txt[0:i_money] and "G" not in txt[txt.index("T")+1:i_money] or "T" in txt[i_money+1:] and "G" not in txt[i_money+1:-1]:
        return "ALARM!"
    if txt.count("$") == 2:
        ri_money = txt.rindex("$")
        if "T" in txt[i_money:ri_money] and "G" not in txt[i_money+1:ri_money] or "T" in txt[ri_money + 1:] and "G" not in txt[ri_money + 1:-1]:
            return "ALARM!"
    return "Safe"

