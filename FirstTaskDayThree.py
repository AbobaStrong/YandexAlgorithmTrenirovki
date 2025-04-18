size = int(input())
arr = [[x, 1] for x in map(int, input().split())]
k = int(input())
queries = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(k)]
n = 0
while 2**n < size:
    n += 1

for i in range(2**n - len(arr)):
    arr.append([float("-inf"), 1])

derevo = [[None, 1] for _ in range(2**n - 1)] + arr

for i in range(len(derevo)//2 - 1, -1, -1):
    left, right = derevo[2*i+1], derevo[2*i+2]
    if left[0] > right[0]:
        derevo[i] = [left[0], left[1]]
    elif left[0] < right[0]:
        derevo[i] = [right[0], right[1]]
    else:
        derevo[i] = [left[0], left[1] + right[1]]



def max_obhod_dereva_na_otrezke(l, r, node=0, node_l=0, node_r=(2 ** n - 1)):
    #полностью входит т.е для [2,6] в узле [3,5]
    if l <= node_l and r >= node_r:
        return derevo[node]
    # [2,6] и [7,8]
    if r < node_l or l > node_r:
        return [float("-inf"), 0]
    #[0,3] и [2,6] или [4,7] и [2,6]
    #здесь пересечение и мы должны проверить детей

    mid = (node_l + node_r) // 2
    left_max = max_obhod_dereva_na_otrezke(l, r, 2 * node + 1, node_l, mid)
    right_max = max_obhod_dereva_na_otrezke(l, r, 2 * node + 2, mid + 1, node_r)
    if left_max[0] > right_max[0]:
        return left_max
    elif right_max[0] > left_max[0]:
        return right_max
    else:
        return [left_max[0], left_max[1] + right_max[1]]

for otrezok in queries:
    print(*max_obhod_dereva_na_otrezke(otrezok[0],otrezok[1]))
