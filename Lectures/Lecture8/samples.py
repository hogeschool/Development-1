n = 11
y = 0

# some combinators (not meant for lesson, only for teacher to draw similarities)
Trans = lambda p: lambda x,y: p(y,x)
FlipX = lambda p: lambda x,y: p(n - 1 - x,y)
FlipY = lambda p: lambda x,y: p(x,n - 1 - y)
Plus = lambda p,q: lambda x,y: p(x,y) or q(x,y)
Times = lambda p,q: lambda x,y: p(x,y) and q(x,y)

# square condition
Square = lambda x,y: True

# hollow square condition
Left = lambda x,y: x == 0
Top = Trans(Left)
Right = lambda x,y: x == n - 1
Bottom = Trans(Right)
HollowSquare = Plus(Plus(Left,Top), Plus(Right,Bottom))

# triangle(s)
Triangle = lambda x,y: x <= y
OtherTriangle = FlipX(Triangle)

# pyramid
Pyramid = Times(Triangle, OtherTriangle)
NaivePyramid = lambda x,y: x <= y and (n - 1 - x) <= y

# circle
Circle = lambda x,y: (x - n / 2) * (x - n / 2) + (y - n / 2) * (y - n / 2) <= n / 2 * n / 2

P = Circle
s = ""
while y < n:
  x = 0
  while x < n:
    if P(x,y):
      s = s + "*"
    else:
      s = s + " "
    x = x + 1
  s = s + "\n"
  y = y + 1

print(s)