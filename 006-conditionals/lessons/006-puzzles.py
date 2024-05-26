"""
if(False):
  print("False") # não é executado

if(True):
  print("True") # é executado

x = -6
if x:
  print("something") # é executado 
"""

"""
k = 15
if (k > 20):
  print(1)
elif (k > 10):
  print(2) # esse será executado
elif (k < 20):
  print(3)
else:
  print(4)
"""

"""
l = 15
if (l < 20):
  print("l<20") # esse será executado
if (l > 20):
  print("l>20")
else:
  print("Who am I?") # esse será executado, faz parte de outro if
"""

"""
a = 10
b = 20

if a > 5:
  if b < 30:
    print("Inner condition met") # esse será executado
  else:
    print("Inner condition not met")
else:
  print("Outer condition not met") 
"""

"""
m = 15

# nada será executado
if m>20:
  if m<20:
    print("m>20")
  else:
    print("Who am I?")
"""

"""
number = 5
if number < 0:
  number = number + 10
number = number + 5
print(number) # Output: 10
"""

"""
number = 5
if number < 0:
  number = number + 10
  number = number + 5
print(number) 
"""

"""
number = 5
if(number%2==0):
  isEven = True
else:
  isEven = False
print(isEven)
"""

"""
x = 10
y = 5
if x > 5 and y < 10:
  print("Condition 1")
elif x == 10 or y == 5:
  print("Condition 2")
else:
  print("Condition 3")
"""

"""
x = 5
if not x == 3:
  print("x is not equal to 3")
else:
  print("x is equal to 3")
"""

# Operador Ternário
number = 4
isEven = True if number % 2 == 0 else False
print(isEven)