# 3.1 리스트란?

---

## 리스트(list), 선형 리스트(linear list)

항목들이 차례로 나열되어 있는 선형 자료구조, 항목들이 위치를 가짐.

## 구조

1. 배열 구조
- 모든 자료가 연속적인 공간에 위치 → 배열의 시작 주소와 한 요소의 크기만 알면 위치를 알 수 있다. == 요소 접근의 시간 복잡도가 O(1)
- 용량 변경이 어렵고, 배열에 데이터를 넣고 빼는 과정이 비효율적

1. 연결된 구조
- 각 요소가 다음 요소의 위치만을 알고 있음 → k번째 요소의 위치를 찾기 위해 시작 항목부터 연결된 줄을 따라 k-1번 움직여야 함 == 요소 접근의 시간 복잡도가 O(n)
- 6장에서 자세하게

# 3.2 파이썬의 리스트

---

## 동적 배열

- 파이썬 리스트는 동적 배열로 구현됨
- 필요한 양보다 큰 메모리를 사용하여 배열의 크기 만큼만 사용함
- 추가적인 공간이 필요할 경우 더 큰 메모리에 복사하여 사용하고, 기존의 메모리를 버림

## 시간복잡도

1. append()
- 메모리 용량이 남은 경우 : 맨 뒤에 바로 삽입됨 → 시간복잡도 O(1)
- 메모리 용량이 부족한 경우 : 새로운 메모리에 모두 복사됨 → 시간복잡도 O(n)

1. insert()
- 맨 앞에 삽입할 경우 : 배열의 요소들이 한 칸 씩 뒤로 밀려남 → 시간복잡도 O(n), 비효율적

1. pop()
- 맨 앞의 요소를 삭제할 경우 : 배열의 요소들이 한 칸 씩 뒤로 밀려남 → 시간복잡도 O(n)
- pop() 맨 뒤의 요소 삭제 : 맨 뒤의 요소가 바로 삭제됨 → 시간복잡도 O(1)

# 3.3 배열로 구현한 리스트

---

## 추상자료형(ADT)

- 데이터 : 크기가 100인 배열
1. 공백 상태 검사 : isEmpty()
2. 포화 상태 검사 : isFull()
3. 원하는 위치의 요소 반환 : getEntry(pos)
4. 원하는 위치에 새로운 항목 삽입 : insert(pos, e)
5. 원하는 위치의 항목 삭제 : delete(pos)

```python
capacity = 100 # 1
array = [None]*100
size = 0

def isEmpty(): # 2
    return size == 0

def isFull(): # 3
    return size == capacity

def getEntry(pos): # 4
    if 0 <= pos < size: 
        return array(pos)
    else: return None
    
def insert(pos, e): # 5
    global size
    if not isFull() and 0 <= pos <= size:
        for i in range(size,pos,-1):
            array[i] = array[i-1]
        array[pos] = e
        size += 1
    else:
        print("유효x")
        exit()

def delete(pos): # 6
    global size
    if not isEmpty() and 0 <= pos < size:
        e = array[pos]
        for i in range(size,pos,-1):
            array[i] = array[i+1]
        size -= 1
        return e
    else:
        print("유효 x")
        exit()
```

## 시간복잡도 분석

1. isEmpty(), isFull() : O(1)
    - 한 번의 비교만 함
2. getEntry() : O(1)
    - 배열에서는 1이지만, 연결 구조에서는 O(n)
3. insert(), delete() : 최악의 경우 O(n)
    - 최악의 경우 모두 옮겨야 함.

## 클래스로 구현

- 클래스를 활용해 리스트의 ADT(추상 자료형)을 구현하면 리스트 객체를 마음대로 만들어 사용할 수 있음.

```python
class ArrayList:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size =0
        
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity
    
    def getEnty(self, pos):
        if 0 <= pos < self.size:
            return self.array[pos]
        else:
            return None
        
    def insert(self, pos, e):
        if not self.isFull() and 0 <= pos <= self.size:
            for i in range(self.size,pos,-1):
                self.array[i] = self.array[i-1]
            self.array[pos] = e
            self.size += 1
        else:
            pass
        
    def delete(self, pos):
        if not self.isEmpty() and 0 <= pos < self.size:
            e = self.array[pos]
            for i in range(self.size,pos,-1):
                self.array[i] = self.array[i+1]
            self.size -= 1
            return e
        else: pass

## 도전 코딩

		def replace(self, pos, e):
        if not self.isEmpty() and 0 <= pos < self.size:
            self.array[pos] = e
        else:
            pass
        
    def count(self, e):
        count = 0
        for i in range(self.size):
            if e==self.array[i]:
                count += 1
            else:
                pass
        return print(count)
        
    def __str__(self): # 문자열 변환 연산자, 중복함수 __str__
        return str(self.array[0:self.size])
```

<aside>
💡 __str__ : 클래스의 객체를 문자열로 바꾸어야 하는 경우 호출되는 함수

</aside>
ex) print()의 매개변수로 리스트 객체를 넣으면 자동으로 객체 내용을 문자열로 변환해줌. 위 예제에서는 리스트를 자동으로 슬라이싱하여 나열해줌.

# 3.5 집합이란?

---

## 개념

- 원소의 중복을 허용하지 않음
- 원소들 사이에 순서가 없음
1. 합집합 A****∪B****
2. 교집합 A ****∩ B****
3. 차집합 A - B

## 추상자료형(ADT)

- 데이터 : 같은 유형의 중복되지 않는 요소들의 모임, 순서는 없지만 비교할 수 있어야 함.
1. contains(e) : 집합이 원소 e를 포함하는지 검사
2. insert(e) : 새로운 원소 e 삽입, 중복 삽입 불가
3. delete(e) : 원소 e를 집합에서 삭제
4. isEmpty() : 공집합인지 검사
5. isFull() : 집합이 가득 차 있는지 검사
6. union(setB) : setB와 합집합을 만들어 반환
7. intersect(setB) : setB와 교집합을 만들어 반환
8. difference(setB) : setB와 차집합을 만들어 반환

# 3.6 집합의 구현

---

```python
class ArraySet:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size =0
        
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity
    
    def contains(self,e): # 찾는 원소 e가 있는가
        for i in range(self.size):
            if self.array[i] == e:
                return True
            return False
    
    def insert(self,e):
        if not self.contains(e) and not self.isFull():
            self.array[self.size] = e
            self.size += 1
    
    def delete(self,e):
        for i in range(self.size):
            if self.array[i] == e:
                self.array[i] = self.array[self.size-1]
                self.size -= 1
                return
    
    def union(self,setB): # 합집합
        setC = ArraySet()
        for i in range(self.size):
            setC.insert(self.array[i])
        for i in range(setB.size):
            if not setC.contains(setB.array[i]):
                setC.insert(setB.array[i])
        return setC
    
    def intersect(self,setB): # 교집합
        setC = ArraySet()
        for i in range(self.size):
            if setB.contains(self.array[i]):
                setC.insert(self.array[i])
        return setC
    
    def difference(self,setB): # 차집합
        setC = ArraySet()
        for i in range(self.size):
            if not setB.contains(self.array[i]):
                setC.insert(self.array[i])
        return setC
    
    def __str__(self):
        return str(self.array[0:self.size])
```

## 시간복잡도

1. contains()
    - 원소를 찾기 위해 배열 전체를 검사, O(n)
2. insert()
    - contains()를 통해 중복 검사를 하기 때문에 결국 O(n)
3. delete()
    - 최악의 경우 마지막에 위치한 원소를 삭제해야 하기 때문에 O(n)
4. union(), intersect(), difference()
    - for문을 통해 전체 요소를 검사하는데, 그 아래서 contains()가 실행되기 때문에 O(n²)
