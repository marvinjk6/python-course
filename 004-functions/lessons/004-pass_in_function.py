# o pass indica que o próximo código não será executado
# o pass pode ser colocado em mais de uma posição e atingir o mesmo resultado
# como indicado nos dois primeiros exemplos
def my_function():
  pass
my_function()

def my_function(): pass
my_function()

# é obrigatório passar o código indentado do for, com o pass é pulado
def print_hello_world(no_of_times):
  for i in range(1,10): pass
print_hello_world(10)