import __future__
from app.hello_world import printing, sum_nums, split_items
import argparse, os, sys, subprocess

parser = argparse.ArgumentParser(description='Hello world! best practices')
parser.add_argument('--test', action='store_true')
parser.add_argument('--print', default=None)
parser.add_argument('--sum-nums', default=None, nargs='+')
parser.add_argument('--split', default=None, nargs='+')
args = parser.parse_args()

if args.test:
    subprocess.run('python -m unittest discover -v')

if args.print is not None:
    arg = args.print
    try:
        arg = int(arg)
    except:
        pass
    printing(arg)

if args.sum_nums is not None:
    sum_value = sum_nums(args.sum_nums)
    print(sum_value)

if args.split is not None:
    split = split_items(*args.split)
    print(split)
