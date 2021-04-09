    # class Solution:


    # def numIdenticalPairs(self, nums: list[int]) -> int:
    #     numGoodPairs = 0
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] == nums[j]:
    #                 numGoodPairs += 1
    #     return numGoodPairs


def maximumWealth(self, accounts: list[list[int]]) -> int:
    maxWealth = 0
    for customer in acounts:
        customerWealth = 0
        for bankAccount in customer:
                customerWealth += bankAccount
                if customerWealth > maxWealth:
                    maxWealth = customerWealth
    return maxWealth

acnts = list([23,345,544,323,55])

las  = maximumWealth(acnts)

print('las')