es_oblongo = lambda n: any(n == i * (i + 1) for i in range(int(n**0.5) + 1))

es_triangular = lambda n: any(n == sum(range(1, i + 1)) for i in range(1, int(n**0.5) + 1))