# Method 1
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numSet = {}
        for idx1 in range(len(numbers)):
            diff = target - numbers[idx1]
            if diff in numSet:
                return [numSet[diff]+1, idx1+1]
            else:
                numSet[numbers[idx1]] = idx1
        return


# Method 2
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) -1
        for num in numbers:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l+1,r+1]
            elif total > target:
                r -= 1
            else:
                l += 1
        return 