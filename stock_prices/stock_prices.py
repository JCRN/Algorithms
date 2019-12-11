#!/usr/bin/python

# 1. Find the current min price value:
#        - current_min_price starts at value stored in arr[0]
#        - replaced by the concurrent lowest value in the array:
#            if(n < current_min_price) then current_min_price = n
# 2. Find the maximum profit:
#        - max_profit is initialized at 0
#        - calculate potential profit for each stock price:
#            profit = (current price - min price)
#                if the current price is larger than the min price
#                else set the current price as the new min price value and profit as 0
# 3. Display the Maximum profit

import argparse


def find_max_profit(prices):
    max_profit = 0
    current_min_price = prices[0]
    for i in range(len(prices - 1)):
        if prices[i] < current_min_price:
            current_min_price = prices[i]
        else:
            profit = prices[i] - current_min_price
            if profit > max_profit:
                max_profit = profit
    return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
