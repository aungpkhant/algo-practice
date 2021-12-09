from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # edge case no prices
        if not prices or len(prices) == 1:
            return 0

        # This array will store the max profit at each day
        profits = [None] * len(prices)
        profits[0] = 0
        currentLowestStockPrice = prices[0]

        # Not account for 0th index
        dayToBuy = 1
        dayToSell = None

        for i in range(1, len(prices)):
            if prices[i] < currentLowestStockPrice:
                currentLowestStockPrice = prices[i]
                dayToBuy = i

            maxProfitForCurrentDay = profits[i - 1]
            if profits[i - 1] < prices[i] - currentLowestStockPrice:
                maxProfitForCurrentDay = max(profits[i - 1], prices[i] - currentLowestStockPrice)
                dayToSell = i

            profits[i] = maxProfitForCurrentDay

        # print out day to buy + day to sell
        print("dayToBuy", dayToBuy)
        print("dayToSell", dayToSell)

        return profits[len(profits) - 1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([0, 6, -3, 7]))
