# 다이나믹 프로그래밍 사용
T = int(input())

# 저장
dp = [0, 1, 2, 4]
count = 3

for _ in range(T):
  test = int(input())

  if (test == 0):
    print(dp[0])
  elif (test == 1):
    print(dp[1])
  elif (test == 2):
    print(dp[2])
  elif (test == 3):
    print(dp[3])
  elif (count > test):
    print(dp[test])
  else:
    while (1):
      tmp = 0

      if (count == test):
        print(dp[count])
        break
      count += 1
      tmp = dp[count - 3] + dp[count - 2] + dp[count - 1]
      dp.append(tmp)


