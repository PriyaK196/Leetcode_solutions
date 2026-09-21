# Test Case 1
a = [1, 3, 5, 7, 9]
n = 5
target = 5

low = 0
high = n - 1
result = -1

while low <= high:
    mid = (low + high) // 2

    if a[mid] == target:
        result = mid
        break
    elif a[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

print("Test Case 1:", result)


# Test Case 2
b = [2, 4, 6, 8, 10]
n2 = 5
target = 7

low = 0
high = n2 - 1
result = -1

while low <= high:
    mid = (low + high) // 2

    if b[mid] == target:
        result = mid
        break
    elif b[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

print("Test Case 2:", result)