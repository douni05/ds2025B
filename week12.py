v, e = map(int, input().split()) #정점, 간선
edges = list()

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

print(edges)

