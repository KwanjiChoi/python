N, L = map(int, input().split())

users = []
for i in range(0, N):
  row = []
  for j in range(0, N):
    row.append(False)
  users.append(row)

for i in range(0, L):
  log = list(map(int, input().split()))
  following = log[1] - 1
  if log[0] == 1:
    followed = log[2] - 1
    users[following][followed] = True

  if log[0] == 2:
    for j in range(0, N):
      if users[j][following]:
        users[following][j] = True

  if log[0] == 3:
    follow_list = []
    for j in range(0, N):
      if users[following][j]:
          for k in range(0, N):
              if users[j][k] and following != k:
                  follow_list.append(k)
    
    for k in follow_list:
        users[following][k] = True


for i in range(0, N):
    for j in range(0, N):
        if users[i][j]:
            print('Y', end = '')
        else:
            print('N', end = '')
    print()