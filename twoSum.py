# METHOD 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1 in range(len(nums)):
            for index2 in range(index1+1,len(nums)):
                total = nums[index1] + nums[index2]
                if total == target:
                    return [index1, index2]
                
# METHOD 2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for idx, num in enumerate(nums):
            diff = target - num
            for diff in prevMap:
                return [prevMap[diff],idx]
            prevMap[num] = idx
        return