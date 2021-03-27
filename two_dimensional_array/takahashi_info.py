inputs = [[1, 0, 1], [2, 1, 2],[1, 0, 1]]

ok = True

if inputs[0][0] - inputs[0][1] != inputs[1][0] - inputs[1][1] or inputs[1][0] - inputs[1][1] != inputs[2][0] - inputs[2][1]:
  ok = False

if inputs[0][1] - inputs[0][2] != inputs[1][1] - inputs[1][2] or inputs[1][1] - inputs[1][2] != inputs[2][1] - inputs[2][2]:
  ok = False

if inputs[0][0] - inputs[1][0] != inputs[0][1] - inputs[1][1] or inputs[0][1] - inputs[1][1] != inputs[0][2] - inputs[1][2]:
  ok = False

if inputs[1][0] - inputs[2][0] != inputs[1][1] - inputs[2][1] or inputs[1][1] - inputs[2][1] != inputs[1][2] - inputs[2][2]:
  ok = False

if ok:
  print('Yes')
else:
  print('No')