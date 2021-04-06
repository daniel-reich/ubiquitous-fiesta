
def months_interval(dateStart, dateEnd):
    monthlist = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    if dateStart > dateEnd:
        dateStart, dateEnd = dateEnd, dateStart
​
    m_lst = []
    mn_lst = []
    cur_date = dateStart
    while cur_date <= dateEnd:
        m_lst.append(cur_date.month - 1)
        if cur_date.month < 12:
            cur_date = datetime.date(cur_date.year, cur_date.month + 1, cur_date.day)
        else:
            cur_date = datetime.date(cur_date.year + 1, 1, cur_date.day)
​
    m_lst = sorted(set(m_lst))
    for i in range(len(m_lst)):
        mn_lst.append(monthlist[m_lst[i]])
​
    return mn_lst

