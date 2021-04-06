
def bowling(pins):
  shot = 1
  score = 0
  frame = 1
  frame_score = [0]*10
  for pin in range(len(pins)):
    score += pins[pin]
    frame_score[frame-1] += pins[pin]
    if shot == 1:
      if pins[pin] < 10:
        shot = 2
      elif pins[pin] == 10:
        if frame < 10:
          score += pins[pin+1] + pins[pin+2]
          frame_score[frame-1] += pins[pin+1] + pins[pin+2]
        else:
          score += sum(pins[pin+1::])
          frame_score[frame-1] += sum(pins[pin+1::])
          break
        frame+=1
    elif shot == 2:
      shot = 1
      if pins[pin] + pins[pin-1] == 10:
        if frame < 10:
          score += pins[pin+1]
          frame_score[frame-1] += pins[pin+1]
        else:
          score += sum(pins[pin+1::])
          frame_score[frame-1] += sum(pins[pin+1::])
          break
      frame += 1
  return score

