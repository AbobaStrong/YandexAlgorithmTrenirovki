size = int(input())
arr_values = list(map(int, input().split()))
k = int(input())
queries = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(k)]

n = 0
while 2 ** n < size:
    n += 1

arr = [[val, idx] for idx, val in enumerate(arr_values)]
for _ in range(2 ** n - len(arr)):
    arr.append([float("-inf"), -1])

derevo = [[None, -1] for _ in range(2 ** n - 1)] + arr

for i in range(len(derevo) // 2 - 1, -1, -1):
    left = derevo[2 * i + 1]
    right = derevo[2 * i + 2]
    if left[0] > right[0]:
        derevo[i] = left
    elif right[0] > left[0]:
        derevo[i] = right
    else:
        derevo[i] = left if left[1] < right[1] else right

def max_obhod_dereva_na_otrezke(l, r, node=0, node_l=0, node_r=(2 ** n - 1)):
    if l <= node_l and r >= node_r:
        return derevo[node]
    if r < node_l or l > node_r:
        return [float("-inf"), -1]

    mid = (node_l + node_r) // 2
    left = max_obhod_dereva_na_otrezke(l, r, 2 * node + 1, node_l, mid)
    right = max_obhod_dereva_na_otrezke(l, r, 2 * node + 2, mid + 1, node_r)

    if left[0] > right[0]:
        return left
    elif right[0] > left[0]:
        return right
    else:
        return left if left[1] < right[1] else right

for l, r in queries:
    value, index = max_obhod_dereva_na_otrezke(l, r)
    print(value, index + 1)
