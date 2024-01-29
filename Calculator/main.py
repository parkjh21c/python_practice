import calculate as cal
from datetime import datetime

# 계산기 시작 안내 문구
print("******* 계산기 (Version 1.0) *******")
print()
print("project start : 2024-01-25")
print("현재 날짜 : ", datetime.now().date())
print()
print()

# 입력
while (1):
  print("식을 입력하세요")
  print("종료하려면 -1을 입력하세요")
  print("ex) 1 + 2")

  calcul_formula = input("계산 식 : ")

  if (calcul_formula == "-1"):
    break

  # 수식을 리스트로 변환
  calcul_formula_list = calcul_formula.split()

  # 계산
  calcul = cal.calculate()

  try:
    calcul_formula_list[0] = calcul.change_type(calcul_formula_list[0])
    calcul_formula_list[2] = calcul.change_type(calcul_formula_list[2])
  except:
    print("옳바르지 않은 수식입니다!")
    print()
    continue

  if (calcul_formula_list[1] == "+"):
    answer = calcul.add(calcul_formula_list[0], calcul_formula_list[2])

  elif (calcul_formula_list[1] == "-"):
    answer = calcul.minus(calcul_formula_list[0], calcul_formula_list[2])

  elif (calcul_formula_list[1] == "*"):
    answer = calcul.multiplication(calcul_formula_list[0], calcul_formula_list[2])

  elif (calcul_formula_list[1] == "/"):
    answer = calcul.division(calcul_formula_list[0], calcul_formula_list[2])

  else:
    print("옳바르지 않은 수식입니다!")

  print(f"값 : {answer}")
  print()