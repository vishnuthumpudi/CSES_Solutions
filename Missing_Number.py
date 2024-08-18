n = int(input()) # Input

l = list(map(int,input().split()))

actual_sum = n * (n + 1) / 2
l_sum = sum(l)

print(int(actual_sum - l_sum))