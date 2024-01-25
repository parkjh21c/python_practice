# 재귀 함수

fibo =[[1, 0], [0, 1]]

T = int(input())

count = 2

for _ in range(T):
  case = int(input())
  
  if (case == 0):
    print("%d %d" %(fibo[0][0], fibo[0][1]))
  elif (case == 1):
    print("%d %d" %(fibo[1][0], fibo[1][1]))
  # 미리 구해 놨을 때
  elif (count > case):
    print("%d %d" %(fibo[case][0], fibo[case][1]))
  else:   # 2이상
    while(1):
      tmp = [0, 0]
      tmp[0] = fibo[count - 2][0] + fibo[count - 1][0]
      tmp[1] = fibo[count - 2][1] + fibo[count - 1][1]
      fibo.append(tmp)

      if (count == case): # 목표값과 같을 때
        print("%d %d" %(fibo[case][0], fibo[case][1]))
        count += 1
        break

      count += 1
