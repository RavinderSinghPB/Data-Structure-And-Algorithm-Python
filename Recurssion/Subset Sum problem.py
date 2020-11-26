def countSubsets(arr, n, sm):
    if n == 0:
        return 1 if sm == 0 else 0
    return countSubsets(arr, n - 1, sm) + countSubsets(arr, n - 1, sm - arr[n - 1])


n, sm = 5, 30
arr = [10, 20, 15, 5, 25]

print(countSubsets(arr, n, sm))

'''
10+20
10+15+5
25+5
'''