
def waterjug(start, goal):
    if not start or not goal or not len(start) == len(goal) == 3:
        return "No solution."
​
    checked_configs = set()  
    from collections import deque
    open_configs = deque()
    open_configs.append(([0, 0, start[2]], 0))
    
    def pour(config, i_from, i_to):
        config = config[:]
        if config[i_from] <= start[i_to] - config[i_to]:
          config[i_to] += config[i_from]
          config[i_from] = 0
        else:
          config[i_from] -= start[i_to] - config[i_to]
          config[i_to] = start[i_to]
​
        return config
​
    
    while open_configs:
        config, ops = open_configs.popleft()
        
        if config == goal:
            return ops
            
        candidates = [
            pour(config, 0, 1),
            pour(config, 0, 2),
            pour(config, 1, 0),
            pour(config, 1, 2),
            pour(config, 2, 0),
            pour(config, 2, 1)
        ]
        
        for c in candidates:
            # simple 'hashing' of configurations - works as long as capacities stay relatively small
            key = c[0]+1000*c[1]+1000000*c[2]
            if not key in checked_configs:
                checked_configs.add(key)
                open_configs.append((c, ops+1))
        
            
    return "No solution."

