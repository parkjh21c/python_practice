import calculate as cal
from datetime import datetime
import time

# 계산기 시작 안내 문구
print("******* 계산기 (Version 1.1) *******")
print()
print("project start : 2024-01-25")
print("현재 날짜 : ", datetime.now().date())
print()
print("************************************")
time.sleep(1)

# 숫자, 기호 순서
count = 0
sign = 0
calcul = cal.calculate()

# 입력
while (1):
  time.sleep(1)
  print()
  print("식을 입력하세요")
  print("종료하려면 'end'를 입력하세요")

  # 기호 입력받기
  if (count % 2 != 0):
    sign = input("기호 : ")
    if (sign == "end"):
      break

  # 숫자 입력받기
  else:
    try:
      num_input = int(input("숫자 : "))
    except:
      break
    
    if (sign == "+"):
      answer = calcul.add(answer, num_input)

    elif (sign == "-"):
      answer = calcul.minus(answer, num_input)

    elif (sign == "*"):
      answer = calcul.multiplication(answer, num_input)

    elif (sign == "/"):
      answer = calcul.division(answer, num_input)
    
    elif (sign == "**"):
      answer = calcul.square(answer, num_input)

    # 기호가 없을 때
    else:
      answer = num_input
  
  count += 1

  print(f"값 : {answer}")
  print()
  print("************************************")
  time.sleep(1)
  