import sys

N = int(sys.stdin.readline())

# 리스트 컴프리헨션
DP = [x for x in range(N + 1)]

if (N > 3):
  for i in range(4, N + 1):
    for j in range(1, int(i**(1/2)) + 1):
      s = j * j

      if (N < s):
        break

      if (DP[i] > DP[i - s] + 1):
        DP[i] = DP[i - s] + 1

print(DP[N])