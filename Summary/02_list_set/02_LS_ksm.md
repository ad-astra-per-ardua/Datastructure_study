## 리스트
리스트는 가장 자유로운 선형 자료구조이다.

list 또는 linear list는 항목들이 차례대로 나열되어 있는 선형 자료구조이다. <br>

각각의 항목들은 순서 또는 위치(position, index)를 가진다 
항목들 사이에 순서가 있다 (index) 라는 점에서 집합(set)과는 다르다. 

Set(집합)은 순서의 개념이 없다. linked로 구현을 따로 해주지않는 이상 linear라고 말하기는 어렵다.
list는 set과는 다르게 원소의 중복도 허용하지 않는다.

추가로 리스트는 임의의 위치에서도 항목의 삽입과 삭제가 가능하다. 하지만 해당 기능은 리스트를 한번 순회하므로 O(n) 이다.

### 리스트의 기능
- append(x)
    리스트의 끝에 항목을 더함
- extend(iterable)
    리스트의 끝에 반복가능한 항목을 추가해서 확장. 거의 사용하지않음
ex)
```py
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
```
- insert(i, x)
    주어진 위치에 항목을 삽입. 첫번째 parameter는 삽입되는 요소가 갖게되는 index값.
    a.insert(0,x) 는 리스트의 처음에 삽입하고, a.insert(len(a), x) 는 a.append(x)와 동등하지만,
    전자는 len(a) 만큼 순회후 insert하는거고 append는 고정으로 마지막에 추가하는 방법이라 **amortized O(1)** 이다.

- remove(x)
    리스트에서 Value가 x와 같은 첫번째 항목을 삭제함. Exception으로 ValueError를 일으킴.
    똑같이 리스트를 한번 순회하므로 O(n)

- pop([i])
    리스트에서 주어진 위치에 있는 항목을 삭제하고, 그 항목을 반환함.
    인덱스를 지정하지않으면, 가령 ex.pop() 이런 형식은 리스트의 마지막 항목을 삭제하고 돌려준다.
    시간복잡도 O(1)

- clear()
    리스트의 모든 항목을 삭제함
    O(n)

- index(x [, start[, end ] ])
    리스트에 있는 항목 중 값이 x와 같은 첫 번째 것의 0부터 시작하는 인덱스를 return 함.
    만약 없으면 ValueError를 일으킴.
    선택적인 인자 start 와 end 는 슬라이스 표기법처럼 해석되고,
    검색을 리스트의 특별한 서브 시퀀스로 제한하는 데 사용됨
    역시 시간복잡도는 O(n)

- count(x)
    리스트에서 x가 등장하는 횟수를 돌려줌
    리스트 전체를 순회하며 해당 value를 count하기때문에 시간복잡도는 O(n)이다

- sort(*, key=None, reverse = false)
    리스트의 항복들을 정렬함. 인자들을 정렬 조건으로 사용가능.
    파이썬은 Tim Sort 정렬을 사용하므로 시간복잡도는 O(n logn) 임
    정렬을 할때는 순회과정을 O(n) 포함하고, 정렬 O(n logn) 과정을 거침 빅오 표기법에 의해 작은것은 소거되므로
    최종적인 정렬의 시간복잡도는 O(n logn)

## 집합(Set)

집합은 리스트와는 다르게 원소의 중복을 허용하지 않으며, 원소들 사이에 순서가 없다. 
또한 원소들이 어떤 위치도 가지지도 않고 일렬로 나열하는 의미도 적용되기 어렵기 때문에 linear Datastructure 라고 보기도 어렵다.

현재 파이썬의 집합 자료구조에는 set과 frozenset 이렇게 두개가 존재한다.
set은 가변형으로 add()나 remove()같은 method를 사용하여 내용을 변경할수있습니다.
frozenset은 불변이고 **해시가능** 합니다. (불변하는 해시값을 갖고, 다른 객체와 비교될수있음을 나타냄)

집합은 여러 가지 방법으로 만들 수 있습니다.
- 중괄호 안에 쉼표로 구분된 요소 나열하기: {'jack', 'sjoerd'}
- 집합 컴프리헨션 사용하기: {c for c in 'abracadabra' if c not in 'abc'}
- 형 생성자 사용하기: set(), set('foobar'), set(['a', 'b', 'foo'])

- add(elem)
    원소 elem 을 집합에 추가합니다.

- remove(elem)
    원소 elem 을 집합에서 제거합니다. elem 가 집합에 포함되어 있지 않으면 KeyError 를 일으킵니다.

- discard(elem)
    원소 elem 이 집합에 포함되어 있으면 제거합니다.

- pop()
    집합으로부터 임의의 원소를 제거해 돌려줍니다. 집합이 비어있는 경우 KeyError 를 일으킵니다.

- clear()
    집합의 모든 원소를 제거합니다.

- union(*others)
    set | other | ...
    집합과 모든 others에 있는 원소들로 구성된 새 집합을 돌려줍니다.

- intersection(*others)
    set & other & ...
    집합과 모든 others의 공통 원소들로 구성된 새 집합을 돌려줍니다.

- difference(*others)
    set - other - ...
    집합에는 포함되었으나 others에는 포함되지 않은 원소들로 구성된 새 집합을 돌려줍니다.

- symmetric_difference(other)
    set ^ other
    집합이나 other에 포함되어 있으나 둘 모두에 포함되지는 않은 원소들로 구성된 새 집합을 돌려줍니다.

- copy()
    집합의 얕은 복사본을 돌려줍니다.

집합을 활용한 알고리즘으로는 Union find, Partition Refinement등이 있습니다.
