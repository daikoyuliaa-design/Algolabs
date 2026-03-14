def radix_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        buckets = [[] for _ in range(10)]
        for x in arr:
            buckets[(x // exp) % 10].append(x)
        arr = [x for bucket in buckets for x in bucket]
        exp *= 10
    return arr

def check(stalls, k, dist):
    count, prev = 1, stalls[0]
    for i in range(1, len(stalls)):
        if stalls[i] - prev >= dist:
            prev = stalls[i]
            count += 1
    return count >= k

def aggressive_cows(stalls, k):
    stalls = radix_sort(stalls)
    lo, hi = 1, stalls[-1] - stalls[0]
    print("[Крайні значення]:")
    print(f" - Найменша відстань (lo): {lo}")
    print(f" - Найбільша відстань (hi): {hi}")
    res = 0
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if check(stalls, k, mid):
            res = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return res

def read_from_file(filename):
    try:
        with open(filename, 'r') as f:
            n, c = map(int, f.readline().split())
            return n, c, list(map(int, f.read().split()))
    except FileNotFoundError:
        print(f"Помилка: Файл {filename} не знайдено.")
        return None
