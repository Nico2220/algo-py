def longestSubarrayWithSumK(a: [int], k: int) -> int:
    start = 0
    end = 0
    sum = 0
    longest = [0, 0]
    while end < len(a):
        sum += a[end]
        while sum > k and start < end:
            sum -= a[start]
            start +=1
        if sum == k and longest[1] - longest[0] + 1 < end - start + 1:
            longest[0] = start
            longest[1] = end
        end +=1

    return longest[1] - longest[0] + 1
