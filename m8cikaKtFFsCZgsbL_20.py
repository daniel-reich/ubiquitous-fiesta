
def water_transfer(source, destination, limit):
    available = limit - destination
    if source <= available:
        return 0, destination + source
    return source - available, limit
​
​
def waterjug(start, goal):
    initial_state = [0, 0, start[2]]
    if initial_state == goal:
        return 0
    elif sum(initial_state) != sum(goal):
        return 'No solution.'
    count = 0
    known_states = [initial_state]
    current_states = [initial_state]
    while current_states:
        new_states = []
        for state in current_states:
            for tpl in [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]:
                new_state = state[:]
                idx_source, idx_destination = tpl
                source_amount = state[idx_source]
                destination_amount = state[idx_destination]
                destination_limit = start[idx_destination]
                if (source_amount > 0 and
                        destination_amount < destination_limit):
                    new_s, new_d = water_transfer(source_amount,
                                                  destination_amount,
                                                  destination_limit)
                    new_state[idx_source] = new_s
                    new_state[idx_destination] = new_d
                    if new_state == goal:
                        return count + 1
                if new_state not in known_states:
                    known_states.append(new_state)
                    new_states.append(new_state)
        current_states = new_states
        count += 1
    return 'No solution.'

