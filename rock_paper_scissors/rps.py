#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  output = []
  choices = ['rock', 'paper', 'scissors']

  def helper(played, rounds):
    if rounds == 0:
      output.append(played)
      return
    
    for i in range(3):
      helper(played + [choices[i]], rounds -1)
  
  helper([], n)
  return output


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')