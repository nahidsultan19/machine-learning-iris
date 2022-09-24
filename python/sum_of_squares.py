def SumOfSquare(nums):
    sum = 0
    for i in nums:
        square = i**2
        sum += square
    return sum


nums = [1, 2, 3, 4, 5, 6]
result = SumOfSquare(nums)
print(result)
