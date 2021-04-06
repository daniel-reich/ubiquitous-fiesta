
def asteroid_collision(asteroids):
  done = False
  print(asteroids)
  while not done:
    original_size = len(asteroids)
    print('Original Size: ' + str(original_size))
    for count, asteroid in enumerate(asteroids):
      if asteroid < 0:
        # Something to the left?
        if count > 0:
          # Evaluate
          if asteroids[count - 1] < 0:
            continue
          elif abs(asteroid) > asteroids[count - 1]:
            del asteroids[count - 1]
          elif abs(asteroid) == asteroids[count - 1]:
            del asteroids[count]
            del asteroids[count - 1]
          else:
            del asteroids[count]
          print(asteroids)
          break
          
    if original_size == len(asteroids):
      print('Final Size: ' + str(len(asteroids)))
      done = True
      
  return asteroids

