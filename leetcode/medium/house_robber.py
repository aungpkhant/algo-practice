from typing import List

# Dyanamic programming problem
# [ 60, 102, 60, 10]
# rob - array[i-2] + currentHouseValue
# not rob - array[i-1]

# Bottom up approach with memoization
# Can optimize space by storing only latest values


class Solution:
    def safeGetArray(self, array, index):
        if index < 0 or index >= len(array):
            return 0
        return array[index]

    def rob(self, nums: List[int]) -> int:

        loot = [0 for i in range(len(nums))]

        for i in range(len(loot)):
            # Current loot + All loot from 2 houses back
            robCurrent = nums[i] + self.safeGetArray(loot, i - 2)
            dontRobCurrent = self.safeGetArray(loot, i - 1)
            loot[i] = max(robCurrent, dontRobCurrent)

        return loot[-1]


solution = Solution()
print(solution.rob([2, 7, 9, 3, 1]))
