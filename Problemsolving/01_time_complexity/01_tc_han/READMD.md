# <img width="20px"  src="https://d2gd6pc034wcta.cloudfront.net/tier/6.svg"> [알고리즘 수업 - 점근적 표기 1](https://www.acmicpc.net/problem/24313)

| 제출 번호 | 닉네임   | 채점 결과    | 메모리  | 시간 | 언어     | 코드 길이 |
| --------- | -------- | ------------ | ------- | ---- | -------- | --------- |
| 67276283  | tkdgml82 | 맞았습니다!! | 31256KB | 48ms | Python 3 | 134 B     |

## 문제

<p>오늘도 서준이는 점근적 표기&nbsp;수업 조교를 하고 있다.&nbsp;아빠가 수업한&nbsp;내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.</p>

<p>알고리즘의 소요 시간을 나타내는 O-표기법(빅-오)을&nbsp;다음과 같이 정의하자.</p>

<p>O(<em>g</em>(<em>n</em>)) = {<em>f</em>(<em>n</em>) | 모든&nbsp;<em>n</em>&nbsp;≥&nbsp;<em>n<sub>0</sub></em>에 대하여&nbsp;<em>f</em>(<em>n</em>) ≤&nbsp;<em>c</em>&nbsp;×&nbsp;<em>g</em>(<em>n</em>)인 양의 상수&nbsp;<em>c</em>와&nbsp;<em>n<sub>0</sub></em>가 존재한다}</p>

<p>이 정의는 실제 O-표기법(<a href="https://en.wikipedia.org/wiki/Big_O_notation">https://en.wikipedia.org/wiki/Big_O_notation</a>)과 다를 수 있다.</p>

<p>함수 <em>f</em>(<em>n</em>)&nbsp;=&nbsp;<em>a<sub>1</sub>n&nbsp;</em>+&nbsp;<em>a<sub>0</sub></em>, 양의 정수&nbsp;<em>c</em>,&nbsp;<em>n<sub>0</sub></em>가 주어질 경우&nbsp;O(<em>n</em>) 정의를 만족하는지 알아보자.</p>

## 입력

<p>첫째 줄에 함수&nbsp;<em>f</em>(<em>n</em>)을 나타내는 정수&nbsp;<em>a<sub>1</sub></em>,&nbsp;<em>a</em><sub><em>0</em></sub>가 주어진다.&nbsp;(0&nbsp;≤ |<em>a<sub>i</sub></em>| ≤ 100)</p>

<p>다음&nbsp;줄에 양의 정수&nbsp;<em>c</em>가 주어진다.&nbsp;(1&nbsp;≤&nbsp;<em>c</em>&nbsp;≤ 100)</p>

<p>다음&nbsp;줄에 양의 정수&nbsp;<em>n<sub>0</sub></em>가 주어진다.&nbsp;(1&nbsp;≤&nbsp;<em>n<sub>0</sub></em>&nbsp;≤ 100)</p>

## 출력

<p>f(n), c, n0가 O(n) 정의를 만족하면 1, 아니면 0을 출력한다.</p>
