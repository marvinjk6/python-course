## operador não igual, diferente (!=)

a = 6
if a != 2:
  print("6 é diferente de 2, valor diferente")

if not a == 2:
  print("6 == 2 -> False, not muda pra True")

# quando falamos de números inteiros, todos retornam True com excessão do 0

print(bool(6))  # True
print(bool(-6))  # True
print(bool(0))  # False