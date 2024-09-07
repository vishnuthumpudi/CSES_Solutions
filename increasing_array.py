def solve(arr, N):
    ans = 0
    for i in range(1, N):
        if arr[i - 1] > arr[i]:
            ans += (arr[i - 1] - arr[i])
            arr[i] = arr[i - 1]
    return ans

n = int(input())
arr = list(map(int,input().split()))
result = solve(arr,n)
print(result)