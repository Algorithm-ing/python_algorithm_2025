def solution(arr):
    answer = []
    for a in arr:
        if not answer:
            answer.append(a)
        else:
            if answer[-1] == a:
                continue
            answer.append(a)
    
    return answer