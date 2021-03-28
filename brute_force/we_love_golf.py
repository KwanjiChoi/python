K = int(input())
A, B = map(int, input().split())
# ans = 'NG'

# for i in range(A, B + 1):
#   if i % K == 0:
#     ans = 'OK'
#     print(i)
#     break

# print(ans)
ans = False

x = A // K
y = B // K

if x < y:
  ans = True

if A % K == 0:
  ans = True

if ans:
  print('OK')
else:
  print('NG')
