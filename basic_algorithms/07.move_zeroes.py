# Test Case 1
a = [0, 1, 0, 3, 12]
n = 5

j = 0

for i in range(n):
    if a[i] != 0:
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
        j += 1

print("Test Case 1:", *a)


# Test Case 2
b = [0, 0, 1]
n2 = 3

j = 0

for i in range(n2):
    if b[i] != 0:
        temp = b[i]
        b[i] = b[j]
        b[j] = temp
        j += 1

print("Test Case 2:", *b)