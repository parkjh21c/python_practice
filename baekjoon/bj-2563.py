N = int(input())

# 0으로 채운다
background = [0 for _ in range(101)]

for _ in range(101):
  background[_] = [0 for i in range(101)]

max_a = 0
max_b = 0

for _ in range(N):
  a, b = map(int, input().split())
  if (a > max_a):
    max_a = a
  if (b > max_b):
    max_b = b
  for i in range(b, b + 10):
    for j in range(a, a + 10):
      background[i][j] = 1

count = 0

for i in range(max_b + 11):
  for j in range(max_a + 11):
    if (background[i][j] == 1):
      count += 1

print(count)