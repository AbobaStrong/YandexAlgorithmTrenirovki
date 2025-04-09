n, m = map(int, input().split())
groups_input = list(map(int, input().split()))
computers = list(map(int, input().split()))

groups = [(val + 1, idx) for idx, val in enumerate(groups_input)]
computers = [(val, idx) for idx, val in enumerate(computers)]

groups.sort()
computers.sort()

p = 0
i = j = 0
result = [0] * n

while i < n and j < m:
    group_size, group_idx = groups[i]
    computer_size, _ = computers[j]
    if group_size <= computer_size:
        p += 1
        result[group_idx] = computers[j][1] + 1
        i += 1
        j += 1
    else:
        j += 1

print(p)
print(*result)
