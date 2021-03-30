N = int(input())

Stock = list(map(int, input().split()))

Q = int(input())

sell = 0

# 全種流販売で販売した1種類あたりの枚数
z = 0

# セット販売で販売した1種類あたりの枚数
s = 0

min_s_Stock = 1000000000

min_z_Stock = 1000000000

# 最小値
for i in range(0, N):

  if i % 2 == 0:
    min_s_Stock = min(Stock[i], min_s_Stock)
    
  else:
    min_z_Stock = min(Stock[i], min_z_Stock)
        
for _ in range(0, Q):
  query = list(map(int, input().split()))
    
  if query[0] == 1:
    x = query[1] - 1
    a = query[2]
        
    if x % 2 == 0:
      card_x = Stock[x] - z - s
    else:
      card_x = Stock[x] - z
        
    if card_x >= a:
      Stock[x] -= a
      sell += a
        
      if x % 2 == 0:
        min_s_Stock = min(Stock[x], min_s_Stock)

      else:
        min_z_Stock = min(Stock[x], min_z_Stock)
    
    elif query[0] == 2:
      a = query[1]
       
      if min_s_Stock - s - z >= a:
        s += a
    
    elif query[0] == 3:
      a = query[1]
        
      if min(min_s_Stock - s - z, min_z_Stock - z) >= a:
        z += a
            
            
for i in range(0, N):
  if i % 2 == 0:
    sell += s
        
        
sell += z * N

print(sell)