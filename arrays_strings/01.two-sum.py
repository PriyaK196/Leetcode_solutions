
def twoSum(numbers, target):
        start=0
        end = len(numbers)-1
        while start < end:
            sum = numbers[start]+numbers[end]
            if sum == target:
                return [start+1,end+1]
            elif sum > target:
                end-=1
            else:
                start+=1
        return [-1,-1]
# Test Case 1
nums = [2, 7, 11, 15]
target = 9

print("Test Case 1:", twoSum(nums, target))


# Test Case 2 - duplicate values
nums = [3, 3]
target = 6

print("Test Case 2:", twoSum(nums, target))