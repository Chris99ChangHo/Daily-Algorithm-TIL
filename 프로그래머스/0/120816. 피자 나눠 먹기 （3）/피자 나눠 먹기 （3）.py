def solution(slice, n):
    if n / slice <= 1:
        answer = 1
    elif n % slice == 0:
        answer = int(n / slice)
    else:
        answer = int(n / slice) + 1
    return answer