# 스택이란?

### 스택은 후입 선출 (Last_In First Out : LIFO)의 자료구조이다.

스택은 입출력이 후입선출의 형태로 일어나는 자료구조를 말한다. 예를 들어 A, B, C, D를 순서대로 입력했다면 꺼낼때는 D, C, B, A 형식으로만 꺼낼 수 있다.

<p align = "center"><img width="300" src = "https://blog.kakaocdn.net/dn/9IxSz/btqPwnswHpv/dasbKBse7eugog7pONcOj1/img.png"></p>

스택의 추상 자료형
스택에는 숫자나 문자열을 포함한 어떤 자료든 저장할 수 있다. 이것은 리스트나 큐, 트리 등과 같은 다른 자료구조들도 마찬가지이다. 그렇다면 스택은 어떤 연산을 지원해야 할까?
스택에서도 삽입과 삭제가 가장 필수적인 연산이다. 이들은 스택의 상태를 변화시킨다. 스택이 비어있는지 꽉 찼는지를 살피거나, 상단 요소를 들여다보는 기능도 있으면 편리하다.

다음은 스택의 추상 자료형이다.

데이터 : 후입선출의 접근 방법을 유지하는 항목들의 모음

- push(e): 요소 e를 스택의 맨 위에 추가한다.
- pop(): 스택의 맨 위에 있는 요소를 꺼내 반환한다.
- isEmpty(): 스택이 비어있으면 True를 아니면 False를 반환한다.
- isFull(): 스택이 가득 차 있으면 True 아니면 False를 반환한다.
- peek(): 스택이 맨 위에 있는 항목을 삭제하지 않고 반환한다.

스택의 삽입과 삭제를 보통 push와 pop이라 부른다. push()를 하면 차례대로 쌓이고 pop()을 하면 맨 위에 있는 데이터 부터 삭제된다.

isEmpty와 isFull은 각각 스택의 공백상태(비어있는 상태)와 포화상태(가득 차 있는 상태)를 검사하는 연산들이다. 스택의 연산들을 적용하다 보면 두가지 오류 상황을 만날 수 있다. 먼저 push()를 실행후 스택의 용량이 꽉 차있다면 오버플로 오류라고 한다. 그리고 참조 불가능한 데이터를 삭제할려고 하면 언더플로 오류가 발생한다.

# 스택의 구현

### 배열을 이용한 스택의 구조

```python
# 전역변수
capacity = 10
array = [None] * capacity
top = -1

# 스택의 연산: 일반 함수
# top이 -1이면 공백상태 true를 반환
def isEmpty():
	if top == -1: return True
	else: return False

def isFull():
	return top == capacity -1

def push(e):
	global top
	# 포화 상태가 아니면 push가능
	if not isFull():
		top += 1
		return array[top] = e
	else:
		print("Stack underflow")
		exit()

def pop():
	global top
	# 공백 상태가 아니면 pop가능
	if not isEmpty():
		top -= 1
		return array[top+1]
	else:
		print("Stack underflow")
		exit()

def peek():
	# peek도 공백상태가 아니어야 가능한다, top 위치의 요소를 반환하면 됨
	if not isEmpty():
		return array[top]
	else: pass
```

### 배열로 구현한 스택 클래스

```python
class ArrayStack:
	def _init_(self, capacity):
		self.capacity = capacity
		self.array = [None] * self.capacity
		self.top = -1

	def isEmpty(self):
		return self.top == -1

	def isFull(self):
		return self.top == self.capacity - 1

	def push(self, e):
		if not self.isFull():
			self.top += 1
			self.array[self.top] = e
		else: pass

	def pop(self):
		if not self.isEmpty():
			self.top -= 1
			return self.array[self.top+1]
		else: pass

	def peek(self):
		if not self.isEmpty():
			return self.array[self.top]
		else: pass
```
