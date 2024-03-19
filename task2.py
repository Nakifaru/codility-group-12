def solution(A):

    for x in range(2):
        max_diff_value = 0
        max_diff = 0
        max_diff_index = 0
        sums = []

        for x in A:
            digits = [*(str(x))]
            sum_digits = 0
            for digit in digits:
                sum_digits += int(digit)
            sums.append(sum_digits)

        for i in range(len(A) - 1):
            if A[i] - sums[i] > max_diff:
                max_diff = A[i] - sums[i]
                max_diff_index = i
                max_diff_value = sums[i]

        A[max_diff_index] = max_diff_value

    return sum(A)

print(solution([100, 101, 102, 103]))
