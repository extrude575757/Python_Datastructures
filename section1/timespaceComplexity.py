class Solution:

    

    def singleNumber(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            currCount = 1
            numToSearch = nums[i]
            for j in range(len(nums)):
                if j == i:
                    continue
                if nums[j] == numToSearch:
                    currCount += 1
            if currCount == 1:
                return numToSearch
        return -1 

    
    def singleNum(self, nums: list[int]) -> int:
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        for element, numOccurence in counts.items():
            if numOccurence == 1:
                return element


    """
    Runtime: 0(n^2)
    Space: 0(n)

    """
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return (d[target - num ], i)
            d[num] = i