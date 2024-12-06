n = int(input())


def bs(target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if mid*mid >= target:
            end = mid - 1
        else:
            start = mid + 1
        # print(q, mid, start, end)

    return start

print(bs(n, 0, n//2))
