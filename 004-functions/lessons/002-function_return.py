

def print_multiplication(n1,n2): # argumentos - variaveis
  print(n1 * n2)

def multiply_numbers(n1, n2): # argumentos - variaveis
  return n1 * n2

product1 = print_multiplication(10, 3) # parametros - valores 
product2 = multiply_numbers(2, 3) # parametros - valores 

print(product1) # none - não possui retorno
print(product2) # 6
""" 
  possui retorno que pode ser usado pelo programa para fazer diversas operações 
  como a soma por exemplo
"""
sum = product2 + 6
print(sum) # 12