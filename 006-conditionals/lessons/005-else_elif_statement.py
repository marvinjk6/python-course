

i = 3

# nada será printado pois o primeiro if é False
if i % 2 == 0:
  print("i is even")

# o bloco else é executado com a condição do if não é atendida
if i % 2 == 0:
  print("i is even")
else:
  print("i is odd")

# o elif serve para adicionar mais uma condição
# pode ser usado muitas vezes
if i == 1:
  print("i is 1")
elif i == 2:
  print("i is 2")
else:
  print("i is not 1 or 2")