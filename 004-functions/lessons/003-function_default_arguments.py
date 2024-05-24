# para passar o valor default é só usar  = valor

def print_string(str="Hello World", times=1):
  for i in range(1, times+1):
    print(str)

print_string()
print_string("Menino", 3)
