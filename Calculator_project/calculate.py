# 계산 함수 모음

class calculate:
  # type 확인 후 변경
  def change_type(self, num : str):
    # 소수
    if ("." in  num):
      num = float(num)
      return num
    elif ("/" in num):
      num_list = num.split('/')
      num = int(num_list[0]) / int(num_list[1])
      return num
    else:
      num = int(num)
      return num


  # 덧셈
  def add(self, num1 : any, num2 : any):
    answer = num1 + num2
    return answer
  
  # 뺄셈
  def minus(self, num1 : any, num2 : any):
    answer = num1 - num2
    return answer

  # 곱셈
  def multiplication(self, num1 : any, num2 : any):
    answer = num1 * num2
    return answer
  
  # 나눗셈
  def division(self, num1 : any, num2 : any):
    answer = num1 / num2
    return answer
  
  # 제곱(승)
  def square(self, num1 : any, num2 : any):
    answer = num1 ** num2
    return answer