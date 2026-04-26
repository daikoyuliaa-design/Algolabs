from collections import defaultdict

def check_gas_supply(cities, storages, pipes):
    graph = defaultdict(list)
    for u, v in pipes:
        graph[u].append(v)

    result = []
    cities_set = set(cities)

    for storage in storages:
        visited = set()
        stack = [storage]
        visited.add(storage)

        while stack:
            current = stack.pop()
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

        unreachable = sorted(list(cities_set - visited))

        if unreachable:
            result.append([storage, unreachable])

    return result
