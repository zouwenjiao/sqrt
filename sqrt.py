# author: Tiffany Timbers
# date: 2020-02-23

"""Calculates and prints the square root of a given number.
Usage: sqrt.py <number>
Options:
<number>    Number for which the square root should be calculated
"""
  
from docopt import docopt
import math

def main(number):
  print(square_root(number))

if __name__ == "__main__":
  main(opt["<number>"])
