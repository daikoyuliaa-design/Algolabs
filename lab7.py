import csv
from collections import deque, defaultdict

class MaxFlow:
    def __init__(self):
        self.graph = defaultdict(dict)

    def add_edge(self, u, v, capacity):
        self.graph[u][v] = capacity
        if v not in self.graph or u not in self.graph[v]:
            self.graph[v][u] = 0

    def bfs(self, source, sink, parent):
        visited = set()
        queue = deque([source])
        visited.add(source)

        while queue:
            u = queue.popleft()

            for v, capacity in self.graph[u].items():
                if v not in visited and capacity > 0:
                    visited.add(v)
                    parent[v] = u
                    queue.append(v)
                    if v == sink:
                        return True
        return False

    def edmonds_karp(self, source, sink):
        parent = {}
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float('inf')
            s = sink

            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

def load_data(filename):
    try:
        with open(filename, 'r', encoding='utf-8', newline='') as f:
            reader = list(csv.reader(f))

            if len(reader) < 3:
                raise ValueError("CSV файл має містити мінімум 3 рядки (ферми, магазини, дороги)!")

            farms = [x.strip() for x in reader[0] if x.strip()]
            shops = [x.strip() for x in reader[1] if x.strip()]
            roads = []

            for row in reader[2:]:
                if not row or len(row) < 3:
                    continue
                u, v, cap = row[0], row[1], row[2]
                roads.append((u.strip(), v.strip(), int(cap)))

            return farms, shops, roads
    except FileNotFoundError:
        print(f"Помилка: Файл {filename} не знайдено.")
        return [], [], []

def calculate_max_flow(filename):
    farms, shops, roads = load_data(filename)
    if not farms or not shops:
        return 0

    mf = MaxFlow()
    source = "SUPER_SOURCE"
    sink = "SUPER_SINK"

    for u, v, cap in roads:
        mf.add_edge(u, v, cap)

    for farm in farms:
        mf.add_edge(source, farm, float('inf'))

    for shop in shops:
        mf.add_edge(shop, sink, float('inf'))

    return mf.edmonds_karp(source, sink)

if __name__ == "__main__":
    total_cars = calculate_max_flow('roads.csv')
    print(f"Максимальна кількість машин: {total_cars}")
