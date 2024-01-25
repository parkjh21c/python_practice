import sys

Deque = []

# class 정의 해보기
class program:
  # X를 덱 앞에 넣기
  def push_front(self, X):
    Deque.insert(0, X)

  # X를 덱 뒤에 넣기
  def push_back(self, X):
    Deque.append(X)

  # 맨 앞 수 빼고 그 수 출력, 없으면 -1 출력
  def pop_front(self):
    if (len(Deque) == 0):
      print("-1")
    else:
      print(Deque[0])
      del Deque[0]

  # 맨 뒷 수 빼고 그 수 출력, 없으면 -1 출력
  def pop_back(self):
    if (len(Deque) == 0):
      print("-1")
    else:
      print(Deque[-1])
      del Deque[-1]

  # 덱에 들어있는 정수 개수
  def size(self):
    print(len(Deque))
  
  # 비어 있는지 확인
  def empty(self):
    if (len(Deque) == 0):
      print("1")
    else:
      print("0")
  
  # 덱의 가장 앞 정수 출력, 없으면 -1
  def front(self):
    if (len(Deque) == 0):
      print("-1")
    else:
      print(Deque[0])
  
  # 덱의 가장 뒤 정수 출력, 없으면 -1
  def back(self):
    if (len(Deque) == 0):
      print("-1")
    else:
      print(Deque[-1])

N = int(input())

for _ in range(N):
  pro = program()
  tmp = []
  # 개행문자 포함한 문자열 입력받음
  order = sys.stdin.readline()
  
  if (" " in order):
    # 문자 숫자 분리(리스트 형)
    tmp = order.split()

    if (tmp[0] == "push_front"):
      pro.push_front(int(tmp[1]))
    elif (tmp[0] == "push_back"):
      pro.push_back(int(tmp[1]))
    elif (tmp[0] == "pop_front\n"):   # 개행문자 포함 되어 있음
      pro.pop_front()
    elif (tmp[0] == "pop_back\n"):
      pro.pop_back()
    elif (tmp[0] == "size\n"):
      pro.size()
    elif (tmp[0] == "empty\n"):
      pro.empty()
    elif (tmp[0] == "front\n"):
      pro.front()
    elif (tmp[0] == "back\n"):
      pro.back()
    else:
      print("잘못 입력")
  else:
    if (order == "pop_front\n"):   # 개행문자 포함 되어 있음
      pro.pop_front()
    elif (order == "pop_back\n"):
      pro.pop_back()
    elif (order == "size\n"):
      pro.size()
    elif (order == "empty\n"):
      pro.empty()
    elif (order == "front\n"):
      pro.front()
    elif (order == "back\n"):
      pro.back()
    else:
      print("잘못 입력")
      