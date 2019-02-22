#!/usr/bin/python

import sys
import itertools

# def making_change_slow(amt, coins, cache={0:1}):
#   for _ in range(amt, 0, -1):
#     all = itertools.product(coins, repeat=amt)
#     correct_ways = [x for x in all if sum(x) == amt]
#     sorted_ways = [sorted(list(x)) for x in correct_ways]
#     unique_ways = []
#     for i in range(0, len(correct_ways)):
#       if sorted_ways[i] not in unique_ways: 
#         unique_ways.append(sorted_ways[i])
#   return unique_ways

def making_change(amount, denom, cache={}):
  coins = [x for x in denom]
  if amount < 0:
    return 0
  elif len(coins) is 1 or amount <= 1:
    return 1
  else:
    result = cache.get(f'{amount}-{coins}')
    if result and result > 0: return cache[f'{amount}-{coins}']
    ways = 0
    while coins[-1] > amount: coins.pop()
    for i in range(amount//coins[-1] + 1):
      ways += making_change(amount - (i * coins[-1]), coins[:-1], cache)
    cache[f'{amount}-{coins}'] = ways
    return ways

# print('5', making_change(5, [1, 5, 10, 25, 50]))
# print('7', making_change(7, [1, 5, 10, 25, 50]))
# print('8', making_change(8, [1, 5, 10, 25, 50]))
# print('9', making_change(9, [1, 5, 10, 25, 50]))
# print('20', making_change(20, [1, 5, 10, 25, 50]))


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")