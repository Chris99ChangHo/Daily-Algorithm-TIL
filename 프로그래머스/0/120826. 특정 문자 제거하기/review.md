# 문제

## 문제 설명
주어진 문자열 my_string에서 특정 문자 letter를 제거한 결과를 반환하는 문제입니다.

## 풀이 방법
이 문제를 해결하는 대표적인 방법은 두 가지가 있습니다:

replace() 내장 함수 사용

반복문을 이용한 필터링

🔸 1. replace() 내장 함수 사용 (가장 간단한 방법)
replace() 함수는 문자열에서 특정 문자를 다른 문자로 변경할 때 사용됩니다.

✅ replace() 문법
python
복사
편집
문자열.replace(바꿀 대상, 새로운 값)
✅ replace()를 이용한 해결
python
복사
편집
def solution(my_string, letter):
    return my_string.replace(letter, "")
✅ 실행 예시
python
복사
편집
print(solution("hello world", "o"))  # "hell wrld"
print(solution("abcdef", "c"))  # "abdef"
"o"가 "hell wrld"에서 제거됨

"c"가 "abdef"에서 제거됨

🔸 2. 반복문을 이용한 문자 제거 (리스트 컴프리헨션 사용)
replace() 함수 없이, 반복문을 사용해서 특정 문자를 제거할 수도 있습니다.

✅ 리스트 컴프리헨션 사용
python
복사
편집
def solution(my_string, letter):
    return "".join([char for char in my_string if char != letter])
✅ 실행 예시
python
복사
편집
print(solution("hello world", "o"))  # "hell wrld"
print(solution("abcdef", "c"))  # "abdef"
💡 리스트 컴프리헨션을 사용해 "letter"가 아닌 문자들만 모아서 다시 문자열로 변환했습니다.

🔹 replace() vs 리스트 컴프리헨션 비교
방법	장점	단점
replace()	간결하고 빠름	문자열에서만 사용 가능
리스트 컴프리헨션	replace() 없이도 해결 가능	코드가 상대적으로 길어질 수 있음
결론: replace()가 더 간단하고 직관적이므로 추천! 하지만, 문자열 조작을 이해하려면 반복문 방식도 알아두면 좋아.

🔹 추가 정리: replace()는 내장 함수인가?
✅ 네, replace()는 파이썬 문자열(str) 내장 메서드(method)입니다.
🚀 하지만 len()처럼 전역 내장 함수(built-in function)는 아니고, 문자열 객체에서만 사용할 수 있는 메서드입니다.

✅ replace()는 문자열 메서드 (str.replace)
python
복사
편집
text = "apple"
print(text.replace("p", "b"))  # "abble"
replace()는 str 타입에서만 사용 가능하므로, 리스트에는 사용할 수 없습니다.
