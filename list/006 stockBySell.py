def maxProfit(price, start, end):
    if end <= start:
        return 0

    profit = 0

    for i in range(start, end):
        for j in range(i + 1, end + 1):
            if price[j] > price[i]:
                curr_profit = price[j] - price[i] + \
                              maxProfit(price, start, i - 1) +\
                              maxProfit(price, j + 1, end)
                profit = max(profit, curr_profit)

    return profit


if __name__ == "__main__":

    arr = [1, 5, 3, 8, 12]

    n = len(arr)

    print("Our Array : ")

    for i in arr:
        print(i, end=" ")

    print("\nMax Profit : ", maxProfit(arr, 0, n - 1))
