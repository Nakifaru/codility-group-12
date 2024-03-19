def solution(A):
    desc = sorted(A, reverse=True)
    answer = []

    i = 0
    for x in desc:
        if x == desc[0] and answer.count(x) < 1:
            answer.append(x)
            i += 1
        elif answer.count(x) < 2 and x != desc[0]:
            if i % 2 == 0:
                answer.insert(0,x)
            else:
                answer.append(x)
        else:
            i += 1

    return len(answer)

print(solution([2, 3, 3, 2, 2, 2, 1]))