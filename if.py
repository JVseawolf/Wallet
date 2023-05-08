# Write code below 💖

q1 = int(input("1 o 2?"))

if q1 == 1:
  a1 = 1
  b1 = 1
  c1 = 0
  d1 = 0
elif q1 == 2:
  a1 = 0
  b1 = 0
  c1 = 1
  d1 = 1
else:
  print("input incorrecto")

q2 = int(input("1, 2, 3 o 4?"))

if q2 == 1:
  a2 = 2
  b2 = 0
  c2 = 0
  d2 = 0
elif q2 == 2:
  a2 = 0
  b2 = 2
  c2 = 0
  d2 = 0
elif q2 == 3:
  a2 = 0
  b2 = 0
  c2 = 2
  d2 = 0
elif q2 == 4:
  a2 = 0
  b2 = 0
  c2 = 0
  d2 = 2
else:
  print("input incorrecto")

q3 = int(input("1, 2, 3 o 4?"))

if q3 == 1:
  a3 = 4
  b3 = 0
  c3 = 0
  d3 = 0
elif q3 == 2:
  a3 = 0
  b3 = 4
  c3 = 0
  d3 = 0
elif q3 == 3:
  a3 = 0
  b3 = 0
  c3 = 4
  d3 = 0
elif q3 == 4:
  a3 = 0
  b3 = 0
  c3 = 0
  d3 = 4
else:
  print("input incorrecto")

a = a1 + a2 + a3
b = b1 + b2 + b3
c = c1 + c2 + c3
d = d1 + d2 + d3

print(a, b, c, d)

if a > b and a > c and a > d:
  print("vas a A")
elif b > a and b > c and b > d:
  print("vas a B")
elif c > a and c > b and c > d:
  print("Vas a C")
else:
  print("Vas a D")