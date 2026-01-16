def topo_sort(deps):
    result = []
    visited = set()

    def visit(n):
        if n in visited:
            return
        visited.add(n)
        for d in deps.get(n, []):
            visit(d)
        result.append(n)

    for k in deps:
        visit(k)
    return result