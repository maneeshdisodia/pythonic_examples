# triplet count to 0
import time


x = [1, -2, 3, 4, 5, -8, -3, 7, 11, 6]
nums1 = [-1, 0, 1, 2, -1, -4]
nums2 = [-25, -10, -7, -3, 2, 4, 8, 10]

def triplets_counts(x):
    ans = []
    '''n^3 time complexity'''
    for a in x:
        for b in x[1:]:
            for c in x[2:]:
                if a + b + c == 0:
                    ans.append((a, b, c))
                else:
                    pass
    return ans

start_time =time.time()

print(triplets_counts(nums1))
print(triplets_counts(nums2))
print("--- %s seconds ---" % (time.time() - start_time))


def three_Sum(num):
    if len(num) < 3: return []
    num.sort()
    result = []
    for i in range(len(num) - 2):
        left = i + 1
        right = len(num) - 1
        if i != 0 and num[i] == num[i - 1]: continue
        while left < right:
            if num[left] + num[right] == -num[i]:
                result.append([num[i], num[left], num[right]])
                left = left + 1
                right = right - 1
                while num[left] == num[left - 1] and left < right: left = left + 1
                while num[right] == num[right + 1] and left < right: right = right - 1
            elif num[left] + num[right] < -num[i]:
                left = left + 1
            else:
                right = right - 1
    return result


start_time =time.time()
print(three_Sum(nums1))
print(three_Sum(nums2))
print("--- %s seconds ---" % (time.time() - start_time))


aa =iter(nums2)
print([aa.__next__()]*2)

