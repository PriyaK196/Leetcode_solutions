#Test Case 1

words1 = ["flower", "flow", "flight"]
n1 = 3

prefix = words1[0]

for i in range(1, n1):j = 0

while (j < len(prefix) and
       j < len(words1[i]) and
       prefix[j] == words1[i][j]):
    j += 1

prefix = prefix[:j]

print("Test Case 1:", prefix)

#Test Case 2

words2 = ["dog", "racecar", "car"]
n2 = 3

prefix = words2[0]

for i in range(1, n2):j = 0

while (j < len(prefix) and
    j < len(words2[i]) and prefix[j] == words2[i][j]):
    j += 1

prefix = prefix[:j]

print("Test Case 2:", prefix)