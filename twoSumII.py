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