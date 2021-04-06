
import re
def palindromic_date(date):
    dd_mm_regex_date = ''.join(re.findall('\d+', date))
    tempswaplist = re.findall('\d+', date)
    tempswaplist[0], tempswaplist[1] =  tempswaplist[1], tempswaplist[0]
    mm_dd_regex_date = ''.join(tempswaplist)
    if dd_mm_regex_date == dd_mm_regex_date[::-1] and mm_dd_regex_date == mm_dd_regex_date[::-1]:
        return True
    else:
        return False

