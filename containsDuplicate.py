class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set(nums)
        return not(len(nums) == len(hashset))