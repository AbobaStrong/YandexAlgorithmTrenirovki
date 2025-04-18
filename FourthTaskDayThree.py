size = int(input())
arr = list(map(int, input().split()))
q = int(input())
queries = []
for _ in range(q):
    query = input().split()
    querier = [query[0]] + list(map(int, query[1:]))
    querier[1] -= 1
    if query[0] == 's':
        querier[2] -= 1
    queries.append(querier)

n = 1
while (1 << n) < size:
    n += 1

size_padded = 1 << n
arr += [float('-inf')] * (size_padded - size)

tree = [0] * (2 * size_padded - 1)

for i in range(size_padded):
    tree[size_padded - 1 + i] = arr[i]

for i in range(size_padded - 2, -1, -1):
    tree[i] = max(tree[2 * i + 1], tree[2 * i + 2])

def query_max(l, r, node=0, node_l=0, node_r=size_padded - 1):
    if r < node_l or l > node_r:
        return float('-inf')
    if l <= node_l and node_r <= r:
        return tree[node]
    mid = (node_l + node_r) // 2
    left = query_max(l, r, 2 * node + 1, node_l, mid)
    right = query_max(l, r, 2 * node + 2, mid + 1, node_r)
    return max(left, right)

def update(pos, value):
    pos += size_padded - 1
    tree[pos] = value
    while pos > 0:
        parent = (pos - 1) // 2
        left = 2 * parent + 1
        right = 2 * parent + 2
        tree[parent] = max(tree[left], tree[right])
        pos = parent

output = []
for query in queries:
    if query[0] == 's':
        l, r = query[1], query[2]
        res = query_max(l, r)
        output.append(str(res))
    else:
        pos, value = query[1], query[2]
        update(pos, value)

print(' '.join(output))
