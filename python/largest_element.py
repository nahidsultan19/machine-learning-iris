# Find the largest element of a list.

def LargestElement(nums):
    largest = nums[0]
    for i in nums:
        if i > largest:
            largest = i
    return largest


nums = [10, 22, 1, 33, 80]
result = LargestElement(nums)
print(result)

# second way
# nums = [10, 22, 1, 33, 80]
# result = max(nums)
# print(result)
