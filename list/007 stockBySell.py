def maxProfit(price, n):
    profit = 0

    for i in range(1, n):

        if price[i] > price[i - 1]:
            profit += price[i] - price[i - 1]

    return profit


if __name__ == "__main__":

    arr = [1, 5, 3, 8, 12]

    n = len(arr)

    print("Our Array : ")

    for i in arr:
        print(i, end=" ")

    print("\nMax Profit : ", maxProfit(arr, n))
