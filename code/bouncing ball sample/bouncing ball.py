import os
import time
from time import sleep

def cls():
  os.system(['clear','cls'][os.name == 'nt'])

y = 10.0
vy = 0.0
dt = 0.05
while (abs(vy) > 0.9) | (y > 0.2):
  new_y = y + vy * dt
  if new_y <= 0.1:
    vy = -vy * 0.7
  else:
    vy -= 9.8 * dt
    y = new_y
  cls()
  screen = ""
  for j in range(0,20):
    for i in range(0,20):
      if (i == 10) & (j == 19 - int(y)):
        screen += "O"
      elif j == 19:
        screen += "-"
      else:
        screen += " "
    screen += "\n"
  print(screen)
  sleep(0.001)

print("Done bouncing!")
raw_input("Press enter to quit.")
