
""" Tipagem dinamica, uma variavel pode mudar de tipo """
a = 5
print(type(a)) # int
a /= 2
print(type(a)) # float

""" Conversão de tipo """
# int()
# float()
"""
  round() - primeiro argumento é o número, segundo a quantidade de casas decimais (opcional)
  4.49 -> 4  -> arredonda para baixo
  4.5 -> 5  -> arredonda para cima

"""

n1 = 5.6
print(int(n1)) # 5

n2 = 10
print(float(n2)) # 10.0

print(round(5.6))  # Output: 6
print(round(5.4))  # Output: 5
print(round(5.5))  # Output: 6
print(round(5.67, 1))  # Output: 5.7
print(round(5.678, 2))  # Output: 5.68