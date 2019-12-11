#!/usr/bin/python

import argparse
import math

def find_max_profit(prices):
  max_profit = -math.inf

  for i in range(len(prices)-1):
    for j in range(i+1, len(prices)):
      value = prices[j] - prices[i]
      if value > max_profit:
        max_profit = value
  
  return max_profit



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))