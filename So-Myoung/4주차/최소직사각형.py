def solution(sizes):
    a = []
    b = []

    for w, h in sizes:
        a.append(max(w, h))
        b.append(min(w, h))

    return max(a) * max(b)


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
