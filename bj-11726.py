# 팩토리얼 함수를 만든 후 DP활용
fact = [1, 1, 2]

def factorial(a):
  tmp = len(fact) - 1

  if (tmp >= a):  # 이미 구하려는 값이 있을 때
    return fact[a]
  else:
    while (1):
      if (tmp == a):
        return fact[a]
      
      tmp += 1
      value = fact[tmp - 1] * tmp
      fact.append(value)


# 조합 계산 함수
def combination(a, b):
  total = 1
    
  total = factorial(a) // (factorial(b) * factorial(a - b))
  
  return total


n = int(input())

answer = 0
# 짝수일 때
if (n % 2 == 0):
  j = n // 2
  for i in range(n // 2, n + 1):
    answer += combination(i, j)
    j -= 1

# 홀수일 때
else:
  j = n // 2
  for i in range((n // 2) + 1, n + 1):
    answer += combination(i, j)
    j -= 1

answer = answer % 10007

print(answer)