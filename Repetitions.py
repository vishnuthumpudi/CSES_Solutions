def solve(S):
    ans = 1
    count = 1

    for i in range(1, len(S)):
        # If the current character is same as the previous
        # character then increment the count
        if S[i] == S[i - 1]:
            count += 1
        else:
            # If the current character is different from
            # the previous character then reset count to 1
            count = 1

        ans = max(ans, count)

    return ans

n = input()
print(solve(n))