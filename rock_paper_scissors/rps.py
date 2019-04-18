#!/usr/bin/python

import sys
import itertools
import functools

# def rock_paper_scissors(n):
#   return [list(x) for x in itertools.product(["rock", "paper", "scissors"], repeat=n)]

def rock_paper_scissors(n):
  options = ['rock', 'paper', 'scissors']
  plays = []

  def generate_plays(num, outcome=[]):
    if num != 0:
      for option in options:
        generate_plays(num - 1, outcome + [option])
    else:
      plays.append(outcome)
  
  generate_plays(n)
  return plays

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')