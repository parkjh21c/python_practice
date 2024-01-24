Deque = []

# class 정의 해보기
class program:
  # X를 덱 앞에 넣기
  def push_front(X):
    Deque.insert(0, X)

  # X를 덱 뒤에 넣기
  def push_back(X):
    Deque.append(X)

  # 맨 앞 수 빼고 그 수 출력, 없으면 -1 출력
  def pop_front():
    if (len(Deque) == 0):
      print("-1")
    else:
      print(Deque[0])
      del Deque[0]

  # 맨 뒷 수 빼고 그 수 출력, 없으면 -1 출력
  def pop_back():
    if (len(Deque) == 0):
      print("-1")
    else:
      print(Deque[-1])
      del Deque[-1]

  # 덱에 들어있는 정수 개수
  def size():
    print(len(Deque))
  
  # 비어 있는지 확인
  def empty():
    if (len(Deque) == 0):
      print("1")
    else:
      print("0")
  
  # 덱의 가장 앞 정수 출력, 없으면 -1
  def front():
    if (len(Deque) == 0):
      print("-1")
    else:
      print(Deque[0])
  
  # 덱의 가장 뒤 정수 출력, 없으면 -1
  def back():
    if (len(Deque) == 0):
      print("-1")
    else:
      print(Deque[-1])

N = int(input())
