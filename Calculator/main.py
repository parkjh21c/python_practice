import calculate as cal

# 계산기 시작 안내 문구
print("******* 계산기 (Version 1.0) *******")
print()
print("project start : 2024 - 01 - 25")
print("현재 날짜 : ")
print()
print()

# 입력
print("식을 입력하세요")

calcul_formula = input("계산 식 : ")

# 불러오기
calcul = cal.calculate()

# 수식을 리스트로 변환
calcul_formula_list = calcul_formula.split()

if (calcul_formula_list[1] == "+"):
  calcul.add(calcul_formula_list[0], calcul_formula_list[2])

