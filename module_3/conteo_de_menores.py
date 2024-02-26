def count_occurrences(arr):
    counts = {}
    for num in arr:
        counts[num] = counts.get(num, 0) + 1
    return [counts.get(num, 0) for num in sorted(counts)]


C = int(input())
for _ in range(C):
    arr = list(map(int, input().split(' ')))
    print(*count_occurrences(arr))