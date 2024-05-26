# break - encerra a execução do programa quando determinada condição é atendida
for i in range(1, 11):
  if i == 5:
    break
  print(i, end=" ")
print("done")
# Output: 1 2 3 4 done

# continue - pula a iteração quando determinada condição é atendida

for i in range(1, 11):
  if i % 2 == 0:
    continue
  print(i, end=" ")
print("done")
# Output: 1 3 5 7 9 done