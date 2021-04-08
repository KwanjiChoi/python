from collections import deque

height, width = list(map(int, input().split()))

sy, sx = list(map(int, input().split()))
gy, gx = list(map(int, input().split()))

Maze = []

for i in range(height):
    row = input()
    Maze.append(row)


sy -= 1
sx -= 1
gy -= 1
gx -= 1

dist = []


for i in range(height):
    dist.append([-1] * width)
    
Q = deque()
Q.append([sy, sx])
dist[sy][sx] = 0

while len(Q) > 0:
    i, j = Q.popleft()
    
    for i2, j2 in [[i + 1, j], [i - 1, j], [i, j + 1],[i, j - 1]]:
        
        if not (0 <= i2 < height and 0 <= j2 < width):
            continue
        
        if Maze[i][j] == '#':
            continue
        
        if dist[i2][j2] == -1:
            dist[i2][j2] = dist[i][j] + 1
            Q.append([i2, j2])

            

print(dist[gy][gx])