"""
for i in range(1, 3):
  for c in range(1, 4):
    print(f"i = {i}, c = {c}")
    
"""

"""
n = 5
for i in range(n):
  for c in range(n):
    print("*", end="")
  print()
"""

for i in range(5):
  for c in range(i+1):
    print("*", end="")
  print()

for i in range(5):
  for c in range(i+1):
    print(i+1, end="")
  print()