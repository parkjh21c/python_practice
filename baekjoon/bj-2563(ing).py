N = int(input())

total = N * 100
paper = [0 for _ in range(N)]

# 입력받아 저장
for i in range(N):
  tmp = list(map(int, input().split()))
  paper[i] = tmp

for i in range(N - 1):
  if (total == 100):
    break
  for j in range(i + 1, N):
    # 왼쪽 꼭짓점
    if (paper[i][0] <= paper[j][0] < paper[i][0] + 10):
      if (paper[i][1] <= paper[j][1] < paper[i][1] + 10):
        temp = ((paper[i][0] + 10) - paper[j][0]) * ((paper[i][1] + 10) - paper[j][1])
        total = total - temp

      elif (paper[i][1] < paper[j][1] + 10 <= paper[i][1] + 10):
        temp = ((paper[i][0] + 10) - paper[j][0]) * ((paper[j][1] + 10) - paper[i][1])
        total = total - temp

    # 오른쪽 꼭짓점
    elif (paper[i][0] < paper[j][0] + 10 <= paper[i][0] + 10):
      if (paper[i][1] < paper[j][1] + 10 <= paper[i][1] + 10):
        temp = ((paper[j][0] + 10) - paper[i][0]) * ((paper[j][1] + 10) - paper[i][1])
        total = total - temp
      
      elif (paper[i][1] <= paper[j][1] < paper[i][1] + 10):
        temp = ((paper[j][0] + 10) - paper[i][0]) * ((paper[i][1] + 10) - paper[j][1])
        total = total - temp

      

print(total)