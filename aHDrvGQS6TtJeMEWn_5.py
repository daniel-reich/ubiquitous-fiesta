
def max_sum_pair(lst):
    m_up, m_down, start, wall = [0, -1, 0], [0, -1, 0], 0, 0
    for i in range(len(lst)):
        if wall <= 0:
            start = i
            wall = lst[i]
        else:
            wall += lst[i]
        if wall > m_down[0]:
            if start != m_up[1]:
                m_down = [wall, start, i]
            else:
                if wall > m_up[0]:
                    m_up = [wall, start, i]
            if m_down > m_up:
                m_up, m_down = m_down, m_up
    mini, wall = 0, 0
    for i in lst[m_up[1]:m_up[2]+1]:
        if wall >= 0:
            wall = i
        else:
            wall += i
        if wall < mini:
            mini = wall
    maxi, wall = 0, 0
    for i in lst[m_up[2]+1:]:
        if wall <= 0:
            wall = i
        else:
            wall += i
        if wall > maxi:
            maxi = wall
    return m_up[0] + max(m_down[0], maxi, -mini)

