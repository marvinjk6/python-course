
i = 1
while i < 11:
  if i == 7:
    break
  i += 1
  print(i, end=" ")
print("done")
# Output 1 2 3 4 5 6 done

i = 1
while i < 11:
  if i % 2 != 0:
    i += 1 # precisa incrementar antes do continue, pois ele volta para o começo do while
    continue  
  print(i, end=" ")
  i += 1
print("done")