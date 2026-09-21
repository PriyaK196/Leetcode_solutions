# Test Case 1
prices = [7, 1, 5, 3, 6, 4]
n = 6

min_price = prices[0]
max_profit = 0

for i in range(1, n):
    if prices[i] < min_price:
        min_price = prices[i]

    profit = prices[i] - min_price

    if profit > max_profit:
        max_profit = profit

print("Test Case 1:", max_profit)


# Test Case 2
prices2 = [7, 6, 4, 3, 1]
n2 = 5

min_price = prices2[0]
max_profit = 0

for i in range(1, n2):
    if prices2[i] < min_price:
        min_price = prices2[i]

    profit = prices2[i] - min_price

    if profit > max_profit:
        max_profit = profit

print("Test Case 2:", max_profit)