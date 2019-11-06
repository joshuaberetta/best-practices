import __future__
from app.__main__ import main
import argparse

parser = argparse.ArgumentParser(description='Hello world! best practices')
parser.add_argument('--print', default=None)
args = parser.parse_args()

if args.print is not None:
    main(args.print)