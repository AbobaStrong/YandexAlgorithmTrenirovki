t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    res = []
    current_len = 0
    current_min = float('inf')

    for num in a:
        current_len += 1
        if num < current_min:
            current_min = num
        if current_min >= current_len:
            continue
        else:
            res.append(current_len - 1)
            current_len = 1
            current_min = num

    if current_len > 0:
        res.append(current_len)

    print(len(res))
    print(' '.join(map(str, res)))
