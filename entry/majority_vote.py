s = 'abbccabbacbbcaa'

na = s.count('a')
nb = s.count('b')
nc = s.count('c')

mx = max(na, nb, nc)

if na == mx:
  print('na')
elif nb == mx:
  print('nb')
elif nc == mx:
  print('nc')