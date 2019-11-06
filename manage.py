import __future__
from app.hello_world import printing, sum_nums
import argparse

parser = argparse.ArgumentParser(description='Hello world! best practices')
parser.add_argument('--print', default=None)
parser.add_argument('--sum-nums', default=None, nargs='+')
args = parser.parse_args()

if args.print is not None:
    arg = args.print
    try:
        arg = int(arg)
    except:
        pass
    printing(arg)

if args.sum_nums is not None:
    # print(args.sum_ints)
    sum_value = sum_nums(args.sum_nums)
    print(sum_value)