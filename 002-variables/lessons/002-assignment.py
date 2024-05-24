# atribuir o valor de uma variavel a outra
i = 5
j = i
print(i, j)

i = 7
print(i, j) # apenas i muda de valor

j = i * 2
print(i, j) # 7 * 2 = 14

# é possível fazer operações com as variáveis
n1 = 5
n2 = 3
sum = n1 + n2
print(n1, n2, sum)

# é possível atualizar o valor de uma variável baseada em seu valor atual
a = 0
# a = a + 1
a += 1 
print(a)

# atribuição múltipla
x = y = z = 10
print(x, y, z) 
