## 3번 문제 (피자 한 판에 다양한 조각 수)
주어진 피자 한 판의 조각 수(slice)와 피자를 먹을 사람 수(n)에 대해, 필요한 최소 피자 수를 계산하는 문제입니다. `//` 연산자를 사용하여 나누기 연산을 효율적으로 처리할 수 있습니다.

**기존 코드**:
```python
def solution(slice, n):
    if n / slice <= 1:
        answer = 1
    elif n % slice == 0:
        answer = int(n / slice)
    else:
        answer = int(n / slice) + 1
    return answer
```

**개선된 코드**:
```python
def solution(slice, n):
    return (n + slice - 1) // slice  # 올림 처리와 동일한 효과
```

**설명**:
`n / slice` 대신 `n // slice`를 사용하여 소수점 이하를 버리고 몫을 구합니다.

n + slice - 1을 사용하여 나머지가 있을 때 올림 처리가 가능하도록 합니다. 이는 나누어 떨어지지 않으면 추가로 한 판이 더 필요하게 만드는 효과를 줍니다.

## 결론:
`//` 연산자를 사용하면 나누기 연산에서 소수점 부분을 자동으로 버리고, `//` 연산자만으로 나누기 결과를 정수로 처리할 수 있어 코드가 간결해지고 효율적입니다.
