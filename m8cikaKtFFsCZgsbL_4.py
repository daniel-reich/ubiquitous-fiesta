
def add_state(s, states, prev_states):
  s = (s[0], s[1], s[2])
  if s in prev_states:
    return
  states.append(s)
  prev_states.add(s)
def waterjug(start, goal):
  goal = (goal[0], goal[1], goal[2])
  states = []
  next_states = [(0, 0, start[2])]
  steps = -1
  prev_states = {(0, 0, start[2])}
  while len(next_states) > 0:
    states = next_states
    next_states = []
    steps += 1
    while len(states) > 0:
      state = states.pop()
      if state == goal:
        return steps
      for i in range(3):
        for i2 in range(3):
          if i != i2:
            new_state = list(state[:])
            diff = min(state[i], start[i2] - state[i2])
            new_state[i] -= diff
            new_state[i2] += diff
            add_state(new_state, next_states, prev_states)
  return "No solution."

