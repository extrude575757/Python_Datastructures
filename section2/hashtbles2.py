def numJewelsInStones(self,jewels: str, stones: str) -> int:
    numJewls = 0
    jewels = set(list(jewels))
    for stone in stones: # O(n)
        if stone in jewels:  # O(1)
            numJewls += 1
        return numJewls


def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
    res = []
    for (i,num)  in enumerate(nums):
        numElementsSmaller = 0
        for (j,otherNum) in enumerate(nums):
            if i == j:
                continue
            if otherNum < num:
                numElementsSmaller += 1
        res.append(numElementsSmaller)
    return res


def smallerThanCur(nums: List[int]) -> List[int]:
    sortedNums  = sorted(nums)
    numMap = {}
    for (i,num) in enumerate(sortedNums):
        if num not in numMap:
            numMap[num] = i
    res = []
    for num in nums:
        res.append(numMap[num])
    return res