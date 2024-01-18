# 에타토스테네스의 체 사용

data = 123456 * 2
arr = [True for i in range(data + 1)]

# 에타토스테네스의 체 알고리즘
for i in range(2, int(data**(1/2)) + 1): 
  # arr[i] 가 소수일 경우
  if (arr[i] == True):
    j = 2
    while (i * j <= data):  # 배수 모두 지우기
      arr[i * j] = False
      j += 1

while (1):
  n = int(input())

  # 0이 입력되면 종료
  if (n == 0):
    break
  
  count = 0
  for i in range(n + 1, 2 * n + 1):
    if (arr[i] == True):
      count += 1

  print(count)
  

