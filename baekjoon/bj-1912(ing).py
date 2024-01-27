# 연속합 DP로 해결 필요
import sys

n = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))

answer = -1000

for i in range(n):
  tmp = 0
  for j in range(i, n):
    tmp += num[j]
    if (tmp > answer):
      answer = tmp
    elif (tmp < 0):
      break
    

print(answer)