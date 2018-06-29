import itertools as it

def better_grouper(inputs, n):
    iters = [iter(inputs)] * n
    return it.zip_longest(*iters)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(better_grouper(nums,6)))

#takewhile example
list(it.takewhile(lambda x: x<5, [1,2,3,2,1,4,6,2,34,5,67,3]))

