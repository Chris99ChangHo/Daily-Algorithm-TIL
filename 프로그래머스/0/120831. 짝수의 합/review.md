## 📌 문제 설명
정수 n이 주어질 때, n 이하의 모든 짝수를 더한 값을 구하는 함수 solution()을 완성해야 합니다.

## 🔍 핵심 개념: range(n + 1)을 사용하는 이유
range(n)은 0부터 n-1까지 반복되기 때문에,
n을 포함시키기 위해선 반드시 range(n + 1) 을 써야 합니다!

* 예:
```python
range(5)       # → 0, 1, 2, 3, 4  
range(5 + 1)   # → 0, 1, 2, 3, 4, 5 ✅ n까지 포함됨
```

## 💡 풀이 코드
```python
def solution(n):
    answer = 0
    for i in range(n + 1):     # n을 포함하기 위해 +1
        if i % 2 == 0:         # 짝수인지 판별
            answer += i        # 누적합
    return answer
```

## ✅ 추가: 리스트 컴프리헨션을 활용한 한 줄 풀이
*더 간단하게도 표현할 수 있어요:
```python
def solution(n):
    return sum([i for i in range(n + 1) if i % 2 == 0])
```

## 🔁 요약
* range(n + 1) → n까지 포함하려면 꼭 +1
* 짝수 확인 → i % 2 == 0
* 누적합 계산
* 간단하게는 sum() + 리스트 컴프리헨션 활용 가능
