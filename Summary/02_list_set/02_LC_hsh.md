# 리스트란

- 리스트란 항목들이 순서대로 나열되어 있고, 각 항목들은 위치를 갖는다.

#### 리스트의 추상 자료형

- 어떤 위치에 항목을 삽입(insert)하거나 삭제(delete)한다.
- 어떤 위치의 항목을 꺼내지 않고 참조(getEntry)한다.
- 리스트가 비어 있는지 또는 가득 차 있는지를 검사한다.

###### 정의

- insert(pos, e): pos위치에 새로운 요소 e를 삽인한다.
- delete(pos): pos위치에 있는 요소를 꺼내고(삭제) 반환한다.
- isEmpty(): 리스트가 비어 있는지를 검사한다.
- isFull(): 리스트가 가득 차 있는지를 검사한다.
- getEntry(pos): pos위치에 있는 요소를 반환한다.

#### 배열과 파이썬 리스트

파이썬은 배열을 직접 제공하지는 않는다. 리스트와 튜플을 배열처럼 사용할 수 있다. 즉, 배열로 자료구조를 구현하기 위해 파이썬 리스트를 사용하는 것이다. 파이썬의 리스트는 자료구조 리스트를 배열구조로 구현한 하나의 사례이기도 하다.

# 파이썬의 리스트

#### 파이썬의 리스트는 스마트한 배열이다.

리스트(list)는 파이썬에서 가장 많이 사용되는 컬렉션 자료형으로 배열과 같이 여러 개의 데이터를 하나로 묶어서 저장하고 처리할 수 있다.

아래는 C언어에서 크기가 5인 정수(int) 배열을 선언하고 초기화하는 C언어 코드이다.

```c
int A[5] = {1, 2, 3, 4, 5};
int B[5] = {0, 0, 0, 0, 0};
```

다음은 python code이다.

```python
A = [1, 2, 3, 4, 5]
B = [0] * 5
```

C언어에서는 배열의 크기를 따로 저장해야된다. 하지만 파이썬 리스트는 그럴 필요가 없다. 내장함수 len을 이용하면 된다.

```python
print('파이썬의 리스트 A의 크키는', len(A))
```

중요한 사실은 C언어에서는 배열의 크기를 늘릴 수 없다. 5개의 배열을 선언했으면 6개의 데이터를 저장할 수 없다. 하지만 파이썬은 가능하게 구현을 했다. 멤버 함수인 append, insert를 사용을 하면 된다. 다음 A 리스트에 데이터를 추가하는 방법이다.

```python
# A = [1, 2, 3, 4, 5, 6]
A.append(6)
# A = [1, 2, 3, 4, 5, 6, 7]
A.append(7)
# A = [0 ,1, 2, 3, 4, 5, 6, 7]
A.insert(0, 0)
# B = [0, 0, 0, 0, 0, 9]
B.insert(9)
```

#### 파이썬의 리스트는 동적 배열로 구현된다.

기본 아이디어는 필요한 양보다 넉넉한 크기의 메모리를 사용하는 것이다. 예를 들어 실제로 크기가 3인 리스트가 필요하더라도 내부적으로 크기가 10인 배열을 할당하고, 맨 앞의 세 항목만 사용하는 것이다. 만일 크기를 계속 추가해서 크기와 용량이 모두 10이이 되고, 이제 남은 공간이 없다고 생각해보자. 파이썬 리스트는 동적 배열(dynamic array)의 개념을 이용한다. 이것은 추가적인 공간이 필요하면 기존의 메모리를 모두 버리고 더 큰 새로운 메모리를 할당해 사용하는 것이다.

<p align = "center"><img src = "https://blog.kakaocdn.net/dn/btkvBi/btrguMZMQKk/2KFfHTAzMgTDgkTMMtScs1/img.png"></p>

- 1번째 : 기존 용량의 두 배의 배열을 할당
- 2번째 : 기본 배열을 값을 복사
- 3번째 : 항목 삽입
- 4번째 : 기존 배열 메모리 해제

이런씩 으로 파이썬의 리스트는 용량을 늘릴 수 있어 편리하지만, 메모리의 낭비를 감수해야된다.

#### 파이썬 리스트 시간 복잡도

- append() 연산
  append() 연산의 시간 복잡도는 상황에 따라 다르다. 남은 용량이 많고 공간이 있으면 O(n)이 소요된다. 하지만 이러한 상황은 가끔씩 발생하기 때문에 O(1)으로 볼수 있다.

- insert() 연산
  만약에 insert(0, 'N')을 해보자. 그러면 리스트안에는 데이터가 5개있다고 하면 맨 첫번째에 넣기 위해서는 뒤에 있는 5개의 데이터를 한칸씩 밀어내고 데이터를 넣어야된다. 그러면 시간 복잡도는 O(n)이다.

- pop() 연산
  삭제연산 pop도 마찬가지이다. pop(0)을 써서 맨 처음에 항목들을 앞으로 당겨 빈칸을 없애야 한다.
  결론적으로 파이썬의 리스트에서 후단 삽입이나 삭제는 효율적이지만 중간이나 전단에 항목을 넣거나 빼는 것은 비효율적이다. 따라서 삽입은 append()를 삭제는 pop(), 또는 pop(-1)을 사용하는 것이 좋다.

# 배열로 구현한 리스트

#### 배열을 이용한 리스트의 구조

```python
# 전역 변수

# 리스트의 용량
capacity = 100
# 100용량 리스트 선언
array = [None]*capacity
size = 0

# 공백상태 확인
def isEmpty():
    if size == 0:
        return True
    else:
        return False

# 포화상태 확인
def isFull():
    return size == capacity

def getEntry(pos):
    # 리스트의 크기가 첫번 째에서 현재 리스트의 크기사이에 있는지 확인
    if pos >= 0 & pos < size:
        return array[pos];
    else:
        return None


def insert(pos, e):
    global size
    if not isFull() and pos >= 0 & pos < size:
        # range(현재 들어있는 데이터의 크기, 넣을 위치, -1씩 줄어든다.)
        # range(50, 3, -1)
        # 50에서 시작해서 2가 될때까지 1씩 줄어든다.
        for i in range(size, pos, -1):
            array[i] = array[i - 1]
        array[pos] = e
        size += 1
    else:
        print("리스트 overflow 또느 유효하지 않은 삽입 위치")
        exit()

def delete(pos):
    global size
    if not isEmpty() and pos >= 0 & pos < size:
        e = array[pos]
        for i in range(pos, size, -1):
            array[i] = array[i + 1]
        size -= 1
        return e
    else :
        print("리스트 underflow 또느 유효하지 않은 삭제 위치")
        exit()
```

- insert() : insert 같은 경우는 값을 넣을 위치의 데이터를 한칸씩밀어서 공간을 만든 후 거기에 데이터를 넣는다.
- delete() : delete 같은 경우는 insert함수와 비슷하지만 삭제할 데이터를 뒤에 있는 데이터들을 땡겨와서 덮어 쉬우는 형식이다.

#### 시간 복잡도 분석

- isEmpty()와 isFull()은 한번의 비교만 필요해서 O(1)이다
- getEntry()은 시간 복잡도가 O(1)이고 연결된 구조는 O(n)이다.
- insert()과 delete()은 최악의 경우가 맨 앞에 넣거나 array[0]을 삭제하면 대부분을 옮겨되기 때문에 이들의 시간 복잡도는 O(n)이다.

# 클래스로 구현

여러개의 리스트로 구현을 할때는 클래스로 구현한 리스트를 사용하는 것이 더 좋은 방법이다.

```python
class ArrayList:
    # 초기화
    def __init__(self, capacity = 100):
        # 리스트의 용량
        self.capacity = capacity
        # 100용량 리스트 선언
        self.array = [None] * capacity
        self.size = 0

        # 공백상태 확인
        def isEmpty(self):
            return self.size == 0

        # 포화상태 확인
        def isFull(self):
            return self.size == capacity

        def getEntry(self, pos):
            # 리스트의 크기가 첫번 째에서 현재 리스트의 크기사이에 있는지 확인
            if pos >= 0 & pos < self.size:
                return self.array[pos];
            else:
                return None

        def insert(self, pos, e):
            if not isFull() and pos >= 0 & pos < self.size:
                # range(현재 들어있는 데이터의 크기, 넣을 위치, -1씩 줄어든다.)
                # range(50, 3, -1)
                # 50에서 시작해서 2가 될때까지 1씩 줄어든다.
                for i in range(self.size, pos, -1):
                    self.array[i] = self.array[i - 1]
                self.array[pos] = e
                self.size += 1
            else:
                pass

        def delete(self, pos):
            if not isEmpty() and pos >= 0 & pos < self.size:
                e = self.array[pos]
                for i in range(self.size, pos, - 1):
                    self.array[i] = self.array[i + 1]
                self.size -= 1
                return e
            else:
                pass

		def __str__(self):
			return str(self.array[0 : self.size])
```

크게 달라진 점은 별로 없어보인다. 하지만 마지막 **\_**str**\_** 같은 경우는 클래스의 객체를 문자열로 바꾸어야 하는 경우 이 함수가 자동으로 호출된다. print()안에 매걔변수로 리스트 객체를 넣으면 자동으로 이 함수를 통해 객체 내용을 문자열로 변환한다. [0 : self.size]경우는 파이썬의 슬라이싱 기능으로 첫번째부터 현재 크기의 리스트를 가르키고 있다.

# 집합

리스트와 비슷한 개념으로 집합이라고 있다. 집합은 <b> 원소의 중복을 허용하지 않으면 원소들 사이에 순서가 없다는 특징</b>이 있다. 집합의 추상 자료형을 살펴보자. 삽입과 삭제는 여전히 중요한 연산이다. 어떤 원소가 집합에 포함되어 있는지를 검사하는것도 원소의 중복을 허용하지 않은 집합에서는 유용할 것이므로 연산으로 추가해야된다.
집합의 연산들인 합집합, 차집합, 교집합등도 추가할 수 있다.
![screenshoot](https://velog.velcdn.com/images%2Fyoojiwon%2Fpost%2F9a9ba0ea-45fb-43dc-9c77-a11cc0943b9f%2Fimage.png)

#### 집합의 구현

ArrayList와 비슷하게 배열을 이용해 직접 구현해보자

##### 원소가 e가 있는 검사하는 contains(e)연산

어떤 원소가 배열에 있는지를 알려면 배열의 원소를 하나씩 비교해보아야 한다. array[0] ~ array[size-1]까지의 원소들을 e와 비교해 같으면 `True`를 반환 같은 원소가 없으면 `False`를 반환

##### 원소를 삽입하는 insert(e)연산

삽입할 원소가 이미 집합에 있다면 삽입할 수 없다. 따라서 삽입을 위해서 `contains()`를 이용하면 된다.
원소들은 맨 뒤에 넣은 것이 가장 유리하다. 배열의 요소들의 이동이 없기 때문이다. 원소가 삽입되면 size가 하나 증가한다.

##### 원소를 삭제하는 delete(e)연산

먼저 삭제를 할려면 삭제할 원소가 있는지를 확인해야 된다. 가장 효율적인 방법은 <b>삭제할 원소와 배열의 맨 뒤로 이동한 원소를 삭제하는 것이다.</b> 이런씩으로 하면 삭제시 많은 원소들의 이동이 필요 없기 때문이다.

```python
class ArraySet:
    # 초기화
    def __init__(self, capacity = 100):
        # 리스트의 용량
        self.capacity = capacity
        # 100용량 리스트 선언
        self.array = [None] * capacity
        self.size = 0

    # 공백상태 확인
    def isEmpty(self):
        return self.size == 0

    # 포화상태 확인
    def isFull(self):
        return self.size == self.capacity

    # 값이 있는지 확인
    def contains(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                return True
            else:
                return False

    def insert(self, pos, e):
        if not self.contains(e) and not self.isFull():
            # 맨뒤에 사입
            self.array[self.size] = e
            self.size += 1

    def delete(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                # 삭제할 원소를 맨 뒤에 넣기
                self.array[i] = self.array[self.size - 1]
                self.size -= 1
            return

    # 합집합
    def union(self, setB):
        setC = ArraySet()
        # setC에다가 전부 원소를 넣는다.
        for i in range(self.size):
            setC.insert(self.size)

        # setC에 넣은 다음에 setC에 없는 것을 값을 다시 찾아서 넣는다.
        for i in range(setB.size):
            if not setC.contains(setB.array[i]):
                setC.insert(setB.array[i])
        return setC

    # 교집합
    def intersect(self, setB):
        setC = ArraySet()
        for i in range(self.size):
            # 값이 겹치는 부분만 setC에 넣음
            if setB.contains(self.array[i]):
                setC.insert(self.array[i])
        return setC

    # 차집합
    def difference(self, setB):
        setC = ArraySet()
        for i in range(self.size):
            # 값이 겹치지 않은 부분만 setC에 들어감
            if not setB.contains(self.array[i]):
                setC.insert(self.array[i])
        return setC

    def __str__(self):
        return str(self.array[0 : self.size])
```

이런씩으로 contains을 이용해서 합집합, 차집합, 교집합을 나타낸다.
