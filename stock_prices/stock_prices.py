#!/usr/bin/python

# 1. Find the current min price value:
#        - current_min_price is initialized at the value stored in arg[0]
#        - current min price will be replaced by the next lower value in arg[]:
#            if value at index i < current_min_price then the current_min_price = value at index i
# 2. Find the maximum profit:
#        - max_profit is initialized at 0
#        - calculate the potential profit for each stock price:#
#                if the current price is larger than the min price: profit = (current price - min price)
#                else set the current_min_price = the current price and profit = 0
# 3. Display the Maximum profit

import argparse


def find_max_profit(prices):
    max_profit = 0
    current_min_price = prices[0]
    for i in prices:
        if i < current_min_price:
            current_min_price = i
        else:
            profit = i - current_min_price
            if profit > max_profit:
                max_profit = profit
    return print(f'the maximum profit that would have been made would be: ${max_profit}')


find_max_profit([1050, 270, 1540, 3800, 2])

#
# if __name__ == '__main__':
#     # This is just some code to accept inputs from the command line
#     parser = argparse.ArgumentParser(description='Find max profit from prices.')
#     parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#     args = parser.parse_args()
#
#     print("A profit of ${profit} can be made from the stock prices {prices}.".format(
#         profit=find_max_profit(args.integers), prices=args.integers))
