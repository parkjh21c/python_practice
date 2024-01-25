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

calcul_formula_list = calcul_formula.split()


# 덧셈
if ("+" in calcul_formula):
  calcul.add()
