
def pop(state):
​
    ballon_size, ballon_position = sum(state), state.index(sum(state))
​
    for i in range(len(state)):
​
        if i <= ballon_position:
            new_value = ballon_size - (ballon_position - i)
​
        else:  # i > ballon_position
            new_value = ballon_size - abs(ballon_position - i)
​
        # state lengh and ballon position doesn't matter:
        state[i] = new_value if new_value >= 0 else 0
​
    return state

