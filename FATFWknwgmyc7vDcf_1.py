
import re
def small_favor(s):
    date_d = re.findall(r'(\d\d.\d\d.\d\d)', s)
    if date_d:
        date_d = date_d[0]
        if date_d[2] in '/.':
            if int(date_d[-2:]) < 25:
                s = s.replace(date_d, date_d[:-2] + '20' + date_d[-2:])
            else:
                s = s.replace(date_d, date_d[:-2] + '19' + date_d[-2:])
    date_w_lst = re.findall(r'(\w+, \d\d. \d\d.)', s)
    if date_w_lst:
        for date_w in date_w_lst:
            if date_w[:3] in ['Jan', 'Feb', 'Mar', 'Apr', 'Oct']:
                if int(date_w[-3:-1]) < 25:
                    s = s.replace(date_w, date_w[:-3] + '20' + date_w[-3:-1]
                                  + date_w[-1])
                else:
                    s = s.replace(date_w, date_w[:-3] + '19' + date_w[-3:-1]
                                  + date_w[-1])
    return s

