# 1.1 자료구조와 알고리즘

---

## 자료구조의 개념

- 스택 : 접시를 쌓아서 관리하는 구조
- 큐 : 맛집의 줄서기 방식
- 트리 : 조직도
- 그래프 : 지하철 노선도와 같은 구조

## 자료구조의 분류

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/bc36d875-7708-4d1d-a02d-b09caf47d438/5c54c4c4-76cb-48ac-991d-667fe605e232/Untitled.png)

- 선형 자료구조 : 일렬로 나열하여 저장하여 자료들 사이에 순서가 있음
    
    ex) 스택, 큐, 덱 등
    
- 비선형 자료구조 : 한 줄로 세우기 어려운 복잡한 관계의 자료
- ex) 트리(폴더, 조직도), 그래프(지도)

## 알고리즘이란?

- 자료구조 : 데이터를 표현하는 방법
    
    ex) 단어가 저장된 배열
    
- 알고리즘 : 효과적으로 문제를 해결하는 절차
    
    ex) 배열에서 원하는 단어를 효과적으로 찾기 위해 알파벳 순으로 정렬되어 있는 것을 이용
    
- 자료구조 + 알고리즘 = 프로그램

## 알고리즘의 조건

- 입력 : 0개 이상
- 출력 : 1개 이상
- 명백성 : 각 명령어의 의미가 명확해야 함
- 유한성 : 한정된 수의 단계 후 반드시 종료되어야 함
- 유효성 : 각 명령어들은 실행 가능한 연산이어야 함

# 1.2 추상 자료형(Abstract Data Type, ADT)

---

## 추상 자료형의 개념

- 어떤 자료가 있는가?
- 어떤 연산이 제공되는가?
- 어떻게 구현하는지는 정의하지 않음
    
    ex) 가방
    
    1. 가방이 다루는 데이터 : 지갑, 필통, 연필, 노트북 등
    2. 가방이 다루는 연산 : 물건을 넣기, 물건을 빼기, 물건의 개수 확인하기, 물건이 있는지 확인하기 등

<aside>
💡 사용자 프로그램에게 구현하기 위한 세부적인 방법이 아닌 간단한 인터페이스만 공개하여 쉽게 사용할 수 있도록 함

</aside>

```python
# 주요 연산 

def insert(bag, e): # 가방에 물건을 넣는 연산
	bag.append(e)

def remove(bag, e): # 가방에서 물건을 빼는 연산
	bag.remove(e)

# 도전 코딩
def numOf(bag, e):
	return bag.count(e)

# 사용자 프로그램

myBag = []

insert(myBag,'지갑') # 가방에 지갑을 넣음
insert(myBag,'휴대폰')
remove(myBag,'지갑') # 가방에서 지갑을 뺌
```

# 1.3 알고리즘 성능 분석

## 실행 시간 측정

```python
import time
myBag = []
start = time.time()

insert(myBag,'지갑')
. . .

end = time.time()
print('실행시간 : ', end-start
```

- 모듈을 활용한 시간 측정과 단점
    1. 구현 필수
    2. 동일한 조건 및 환경
    3. 동일한 데이터
    

## 알고리즘 복잡도 분석

<aside>
💡 연산 횟수를 대략적으로 계산하여 알고리즘을 구현하지 않고도 알고리즘의 효율성을 평가하는 방법

</aside>

```python
# n까지의 합을 구하는 방법

# 방법 1 : 반복 활용
calc_sum1(n)
	sum = 0 # 연산자 '=' 1번 수행
	for i in range(len(n)): # 반복 연산 무시
		sum = sum + i # 연산자 '='와 '+'가 각각 n번씩 수행
	return sum

# 방법 2 : 공식 활용
calc_sum2(n)
	sum = n * ( n+1 ) / 2 # 연산자 '=', '*', '+', '/'가 각각 1번씩 수행
	return sum
```

- 복잡도 함수 T(n) : 연산들의 실행 횟수, 입력의 크기 n에 대한 함수 형태
    
    방법_1 : T(n) = 2n + 1
    
    - 입력  크기 n에 비례하는 수의 연산 실행
    
    방법_2 : T(n) = 4
    
    - 입력의 크기 n과 관계없이 항상 같은 연산 수행

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/bc36d875-7708-4d1d-a02d-b09caf47d438/34227619-e2a4-4ed4-b5ce-13f57b7a182b/Untitled.png)

- 입력의 크기가 커질수록 방법_2가 효율적임.

## 복잡도의 점근적 표기

<aside>
💡 알고리즘의 복잡도를 단순화 시키는 표기법

</aside>

- 연산량이 얼마나 빨리 증가하는가? = 증가속도를 의미

ex) 2n + 1 → n

ex) 8n² + 2n + 17 → n²

- 복잡도를 단순화 시키는 이유
    
    Ta(n) = 65536n + 2000000
    
    Tb(n) = n² + 2n
    
    - 다음과 같은 경우 n이 작을 때는 Tb(n)가 더 효율적으로 보일 수 있으나 n의 크기가 일정 이상이 되면 Ta(n)의 효율성이 증가하고, Tb(n)의 효율성이 급격하게 나빠짐을 알 수 있음
    - 만약 n이 무한대에 가까워지면 최고차항을 제외한 나머지 항은 영향을 크게 미치지 못함
    - 따라서 최고차항을 단순하게 표현하여 알고리즘의 복잡도를 설명함

## 빅오(big-O) 표기법

<aside>
💡 O(g(n)), 증가 속도가 g(n)과 같거나 낮은 모든 복잡도 함수 포함

</aside>

ex) 2n+1 : O(n)에 속한다, O(n)이다

ex) 0.00001n³ : O(n²)에 속하지 않는다.

- 처리 시간의 상한을 의미

## 빅오메가(big-omega) 표기법

<aside>
💡 **Ω**(g(n)), 증가 속도가 g(n)과 같거나 높은 모든 복잡도 함수 포함

</aside>

ex) 2n³ + 1 : O(n²)에 속한다.

ex) 2n + 1 : O(n²)에 속하지 않는다. 

- 처리 시간의 하한을 의미

## 빅세타(big-theta) 표기법

<aside>
💡 θ(g(n)), 증가 속도가 g(n)과 같은 복잡도 함수만을 포함

</aside>

ex) 2n² + 1 : O(n²)에 속한다.

ex) ex) 2n³ + 1 : O(n²)에 속하지 않는다.

## 표기법 비교

1. 빅세타 표기법 : 정확한 시간 복잡도 계산이 가능할 경우
2. 빅오 표기법 : 상한을 구해 최악의 상황을 고려한 해결책 찾기
3. 빅오메가 표기법 : 하한을 구함

## 복잡도 분석의 예

```python
# 순차 탐색 함수 : 배열에서 어떤 값의 위치 찾기
def search(A, key):
	n = len(A) # 입력의 크기, 1번
	for i in range(n): # 배열의 크기만큼 수행, 입력의 크기 = 배열의 크기
		if A[i] == key: # for문이 반복될 때마다 '==' 연산 수행
			return i # 1번
	return -1 # 1번
```

1. 입력의 크기과 가장 많이 수행되는 기준 연산 찾기
    - 가장 많은 연산을 수행하는 4번 줄 ‘==’을 기준으로 잡기
2. 최선, 최악, 평균적인 경우 계산
    - 최선 : 첫 번째 항목이 key가 되어 한 번만에 탐색, Tᵦₑₛₜ(n) =  1
    - 최악 : 마지막 항목이 key이거나 key가 없는 경우 Tᴡᴏʀsᴛ(n) = n
    - 평균 : 명확하지 않음
- 최선 : O(1)
- 최악 : O(n)
