n = 10
s = ""
i = 0
while i <= n:
  s = s + "*"
  i = i + 1
print(s)

n = 10
s = ""
i = 0
while i <= n:
  if i % 2 == 0:
    s = s + "*"
  else:
    s = s + " "
  i = i + 1
print(s)

n = 5
i = 0
s = ""
while i <= n:
  j = 0
  while j <= n:
    s = s + "*"
    j = j + 1
  s = s + "\n"
  i = i + 1
print(s)

n = 5
i = 0
s = ""
j = 0
while j <= n:
  s = s + "*"
  j = j + 1
s = s + "\n"
while i <= n - 2:
  j = 0
  s = s + "*"
  while j <= n - 2:
    s = s + " "
    j = j + 1
  s = s + "*"
  s = s + "\n"
  i = i + 1
j = 0
while j <= n:
  s = s + "*"
  j = j + 1
s = s + "\n"
print(s)

n = 5
i = 0
s = ""
while i <= n:
  j = 0
  while j <= i:
    s = s + "*"
    j = j + 1
  s = s + "\n"
  i = i + 1
print(s)

n = 5
s = ""
b = n
a = 1
i = 0
while i <= n:
  j = 0
  while j < b:
    s = s + " "
    j = j + 1
  j = 0
  while j < a:
    s = s + "*"
    j = j + 1
  a = a + 2
  b = b - 1
  s = s + "\n"
  i = i + 1
print(s)

import math
n = 10
c = n / 2
i = 0
s = ""
while i <= n:
  j = 0
  while j <= n:
    if math.sqrt((i-c) * (i-c) + (j - c) * (j - c)) < n / 2:
      s = s + "*"
    else:
      s = s + " "
    j = j + 1
  s = s + "\n"
  i = i + 1
print(s)
