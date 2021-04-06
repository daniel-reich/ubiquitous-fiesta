
def spartans_cipher(message, n_slide):
  message = message + " " * (n_slide - (len(message) % n_slide or n_slide))
  n = len(message) // n_slide
  scytale = [list(message[n * i:n * (i + 1)]) for i in range(n_slide)]
  return "".join(sum(zip(*scytale), ())).strip()

