import __future__
from app.__main__ import main
import argparse

parser = argparse.ArgumentParser(description='Hello world! best practices')
parser.add_argument('--print', default=None)
args = parser.parse_args()

if args.print is not None:
    arg = args.print
    try:
        arg = int(arg)
    except:
        pass
    main(arg)
else:
    print('Try printing something to the console using --print "something"')