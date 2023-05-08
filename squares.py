for i in range(1,101):
  
  if i % 3 == 0 and i % 5 == 0:
    print("bizz fuzz")
  elif i % 5 == 0:
    print("fuzz")
  elif i % 3 == 0:
    print("bizz")
  else:
    print(i)

