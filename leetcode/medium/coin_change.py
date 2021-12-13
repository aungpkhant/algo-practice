# Dyamic Programming

from typing import List
import math

# amount - 11
#      [0,1,2,3,4,5,6,7,8,9,10,11]
# $ 1  [0,1,2,3,4,5,6,7,8,9,10,11]
# $ 2  [0,1,1,2,2,3,3,4,4,5,5 ,6]

# Use the array to store lowest number of coins for amount w/ the given coins
# For example, array[1][5] stores lowest number of coins to achieve 6$ using $1 and $2 coins
# To get [x][y]
# 1. [x-1][y] - optimal number of coins using all previous coins
# 2. [x][y - value of current coin] - optimal number of coins using all previous coins + coin at [x]
# Take the max (Scenario 1, Scenario 2)


class Solution:
    def safeGetArray(self, array, row, column):
        # Check for out of bounds
        if row < 0 or column < 0 or row > len(array) or column > len(array[row]):
            return None
        return array[row][column]

    def coinChange(self, coins: List[int], amount: int) -> int:

        coins.sort()

        #  create empty 2D array
        optimalNumberOfCoinsArray = [[math.inf for i in range(amount + 1)] for j in range(len(coins))]

        # setup base cases
        # if amount is 0, we need 0 number of coins doesnt matter what coins
        for row in optimalNumberOfCoinsArray:
            row[0] = 0

        # calculate the first row
        for amount in range(len(optimalNumberOfCoinsArray[0])):
            smallestCoin = coins[0]
            optimalNumberWithOnlySmallestCoin = math.inf

            if amount % smallestCoin == 0:
                optimalNumberWithOnlySmallestCoin = amount // smallestCoin

            optimalNumberOfCoinsArray[0][amount] = optimalNumberWithOnlySmallestCoin

        # calculate next row
        for currentCoinIndex in range(1, len(coins)):
            currentCoin = coins[currentCoinIndex]
            for amount in range(len(optimalNumberOfCoinsArray[currentCoinIndex])):
                prevCoinsOptimal = self.safeGetArray(optimalNumberOfCoinsArray, currentCoinIndex - 1, amount)
                withCurrentCoinOptimal = self.safeGetArray(
                    optimalNumberOfCoinsArray, currentCoinIndex, amount - currentCoin
                )
                if prevCoinsOptimal is None:
                    prevCoinsOptimal = math.inf

                if withCurrentCoinOptimal is None:
                    withCurrentCoinOptimal = math.inf

                withCurrentCoinOptimal += 1

                optimalNumberOfCoinsArray[currentCoinIndex][amount] = min(prevCoinsOptimal, withCurrentCoinOptimal)

        return -1 if optimalNumberOfCoinsArray[-1][-1] == math.inf else optimalNumberOfCoinsArray[-1][-1]


solution = Solution()
print(solution.coinChange([1, 2, 5], 11))
