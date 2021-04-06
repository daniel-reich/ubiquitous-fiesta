
def sun_loungers(beach):
    if '1' not in beach:
        return (len(beach) + 1) // 2
    ans = 0
    if beach[0] == '0':
        first1 = beach.find('1')
        ans += first1 // 2
        beach = beach[first1:]
    beach = beach[::-1]
    if beach[0] == '0':
        first1 = beach.find('1')
        ans += first1 // 2
        beach = beach[first1:]
    for stretch in [len(_) for _ in beach.replace('1', ' ').split()]:
        if stretch >= 3:
            ans += (stretch - 1) // 2
    return ans

