import calculate as cal
from datetime import datetime
import time

# 계산기 시작 안내 문구
print("******* 계산기 (Version 1.0) *******")
print()
print("project start : 2024-01-25")
print("현재 날짜 : ", datetime.now().date())
print()
print("************************************")
time.sleep(1)

# 숫자, 기호 순서
count = 0
calcul = cal.calculate()

# 입력
while (1):
  print("식을 입력하세요")
  print("종료하려면 -1을 입력하세요")

  # 숫자 입력받기
  if (count % 2 == 0):
    num_input = int(input("값 : "))


  # 기호 입력받기
  else:
    sign = input("값 : ")

  # 여기서부터 수정 필요

  if (sign == "+"):
    answer = calcul.add(answer, calcul_formula_list[i + 1])

  elif (sign == "-"):
    answer = calcul.minus(answer, calcul_formula_list[i + 1])

  elif (sign == "*"):
    answer = calcul.multiplication(answer, calcul_formula_list[i + 1])

  elif (sign == "/"):
    answer = calcul.division(answer, calcul_formula_list[i + 1])
  
  elif (sign == "**"):
    answer = calcul.square(answer, calcul_formula_list[i + 1])

  else:
    print("옳바르지 않은 수식입니다! (오류코드 1)")
    print()
    print("************************************")
    time.sleep(1)
    continue



  

  # 숫자 or 기호 받을건지 계산
  count = 0

  if (count % 2 == 1):
    if (calcul_formula_list[i] == "+"):
      answer = calcul.add(answer, calcul_formula_list[i + 1])

    elif (calcul_formula_list[i] == "-"):
      answer = calcul.minus(answer, calcul_formula_list[i + 1])

    elif (calcul_formula_list[i] == "*"):
      answer = calcul.multiplication(answer, calcul_formula_list[i + 1])

    elif (calcul_formula_list[i] == "/"):
      answer = calcul.division(answer, calcul_formula_list[i + 1])
    
    elif (calcul_formula_list[i] == "**"):
      answer = calcul.square(answer, calcul_formula_list[i + 1])

    else:
      print("옳바르지 않은 수식입니다! (오류코드 1)")
      print()
      print("************************************")
      time.sleep(1)
      continue

  


  # 계산


  try:
    for i in range(0, calcul_formula_lest_len, 2):
      calcul_formula_list[i] = calcul.change_type(calcul_formula_list[i])

  except:
    print("옳바르지 않은 수식입니다! (오류코드 0)")
    print()
    print("************************************")
    time.sleep(1)
    continue
  
  answer = calcul_formula_list[0]

  # 기호만 검사
  for i in range(1, calcul_formula_lest_len, 2):
    if (calcul_formula_list[i] == "+"):
      answer = calcul.add(answer, calcul_formula_list[i + 1])

    elif (calcul_formula_list[i] == "-"):
      answer = calcul.minus(answer, calcul_formula_list[i + 1])

    elif (calcul_formula_list[i] == "*"):
      answer = calcul.multiplication(answer, calcul_formula_list[i + 1])

    elif (calcul_formula_list[i] == "/"):
      answer = calcul.division(answer, calcul_formula_list[i + 1])
    
    elif (calcul_formula_list[i] == "**"):
      answer = calcul.square(answer, calcul_formula_list[i + 1])

    else:
      print("옳바르지 않은 수식입니다! (오류코드 1)")
      print()
      print("************************************")
      time.sleep(1)
      continue

  print(f"값 : {answer}")
  print()
  print("************************************")
  time.sleep(1)
  