a = [[84, 97, 66],[79, 89, 11],[61, 59, 7]]
num = 7
inputs = [89, 7, 87, 79, 24, 84, 30]

M = []

for i in range(0, 3):
  row = []
  for j in range(0, 3):
    row.append(False)
  M.append(row)

for i in range(0, num):
  for j in range(0, 3):
    for k in range(0, 3):
      if a[j][k] == inputs[i]:
        M[j][k] = True


bingo = False

for i in range(0, 3):
  if M[i][0] and M[i][1] and M[i][2]:
    bingo = True

for i in range(0, 3):
  if M[0][i] and M[1][i] and M[2][i]:
    bingo = True

if M[0][0] and M[1][1] and M[2][2]:
  bingo = True

if M[0][2] and M[1][1] and M[2][0]:
  bingo = True

if bingo == True:
  print('Yes')
else:
  print('No')

