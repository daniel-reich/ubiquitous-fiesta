
def champions(teams):
    stats, goal_diff = {}, {}
    for t in teams:
        stats[t['name']] = (3 * t['wins']) + (0 * t['loss']) + (1 * t['draws'])
        goal_diff[t['name']] = t['scored'] - t['conceded']
        
    points = {v: 0 for v in stats.values()}
    for v in stats.values():
        points[v] += 1
        
    if any(points[p] >= 2 for p in points):
        x, y = [n['name'] for n in teams if stats[n['name']] == max(points)]
        return max(x, y, key=goal_diff.get)
​
    return max(stats, key=stats.get)

