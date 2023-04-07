class CalculateProfit:
    def calculate_max_profit(self, prices: list) -> int:
        if len(prices) <= 1:
            return 0
        profit = 0
        low = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < low:
                low = prices[i]
            else:
                profit = max(prices[i] - low, profit)
        return profit


if __name__ == '__main__':
    calculate_profit = CalculateProfit()

    input_data = [7, 1, 5, 3, 6, 4]  # [7,6,4,3,1]

    print('So calculated max profit is', calculate_profit.calculate_max_profit(input_data))
