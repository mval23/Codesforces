def mushh(caso):
    right, left = caso[-1], caso[0]
    j, k = 1, -2
    while j != len(caso) + k + 1:
        if left < right:
            left += caso[j]
            j += 1
        elif left >= right:
            right += caso[k]
            k -= 1
    return abs(left - right)


C = int(input())
for i in range(C):
    print(mushh(tuple(sorted(map(int, input().split(', '))))))