"""
for i in range(1, 10):
  print(i) # 1 ate 9
"""

"""
# se passar um argumento é onde para, o ínicio será 0
for i in range(4):
  print(i)
"""

# help(range)

"""
# com step
for i in range(1, 11, 2):
  print(i)
"""

"""
for i in range(1, 11):
  print(i * i)
"""

cont = 0
sum = 0
for i in range(1, 11):
  cont += 1
  sum += i
print(cont, sum)


