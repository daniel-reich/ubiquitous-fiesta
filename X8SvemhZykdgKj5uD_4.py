
letter_at_position = lambda x: 'invalid' if x % 1 \
  or x not in range(1, 27) else chr(int(x) + 96)

