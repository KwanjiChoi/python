# 隣接行列での解法

N, M, P = map(int, input().split())


graph = []

for i in range(0, N):
  row = []
  graph.append(row)

for i in range(0, M):
  u, v = map(int, input().split())

  u -= 1
  v -= 1

  graph[u].append(v)
  graph[v].append(u)


Color = list(map(int, input().split()))

for i in range(0, P):
  query = list(map(int, input().split()))
  if query[0] == 1:
    x = query[1] - 1

    print(Color[x])

    for i in graph[x]:
      Color[i] = Color[x]
  
  if query[0] == 2:
    x = query[1] - 1
    y = query[2]

    print(Color[x])

    Color[x] = y