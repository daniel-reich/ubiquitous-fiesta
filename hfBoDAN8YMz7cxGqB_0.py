
def we_have_house(hh, hw, hd, rh):
    gray_paint = 4*(hw+hd)-6
    yellow_paint = (hw+hd)*2*(hh-2)+hw*rh-111
    if hw < 15 or hd < 11 or hh < 8:
        return ("House too small.")
    if hw > 44 or hd > 44:
        return("House too big.")
    if hh + rh > 20:
        return("No permission.")
    else:
        return("Yellow: " + str(yellow_paint) + ", Gray: " + str(gray_paint))

