T = int(input())

# 쿼터, 다임, 니켈, 페니
coin = [25, 10, 5, 1]

for _ in range(T):
  change = [0, 0, 0, 0]

  C = int(input())

  for i in range(len(change)):
    change[i] = C // coin[i]
    C = C % coin[i]
  
  print("%d %d %d %d" %(change[0], change[1], change[2], change[3]))

