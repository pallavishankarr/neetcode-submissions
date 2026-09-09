class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # go through list, subtract target from that number and check if that number exists in the list
        seen = {}
        
        for index, value in enumerate(nums):
            difference = target - nums[index]

            if difference in seen:
                return [seen[difference], index]

            seen[value] = index

        