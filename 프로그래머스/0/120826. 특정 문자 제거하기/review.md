# 특정 문자 제거하기

## 문제 설명
주어진 문자열 my_string에서 특정 문자 letter를 제거한 결과를 반환하는 문제입니다.

## 해결 방법
1. `replace()` 내장 함수 사용
2. `반복문`을 이용한 필터링

**replace() 내장 함수 사용 (가장 간단한 방법)**
`replace()` 함수는 문자열에서 특정 문자를 다른 문자로 변경할 때 사용됩니다.
replace() 문법: `문자열.replace(바꿀 대상, 새로운 값)`

**예시 코드**
```python
def solution(my_string, letter):
    return my_string.replace(letter, '')
```

**반복문을 이용한 문자 제거 (리스트 컴프리헨션 사용 가능)**
`replace()` 함수 없이, 반복문을 사용해서 특정 문자를 제거할 수도 있습니다.

**예시 코드1**
```python
def solution(my_string, letter):
    answer = ''
    for string in my_string:
        if string != letter:
            answer += string
    return answer
```
    
**예시 코드2**
```python
def solution(my_string, letter):
    return "".join([char for char in my_string if char != letter])
```

## replace() vs 리스트 컴프리헨션 비교
`replace()`는 간결하고 빠르지만 문자열에서만 사용 가능
`리스트 컴프리헨션`은 replace() 없이도 해결이 가능하지만 코드가 상대적으로 길어질 수 있음
결론: replace()가 더 간단하고 직관적 하지만, 문자열 조작을 이해하려면 반복문 방식도 알아두기

## 추가 정리: replace()는 내장 함수인가?
replace()는 파이썬 문자열(str) 내장 메서드(method)입니다. 하지만 len()처럼 전역 내장 함수(built-in function)는 아니고, 문자열 객체에서만 사용할 수 있는 메서드입니다.

replace()는 str 타입에서만 사용 가능하므로, 리스트에는 사용할 수 없습니다.
