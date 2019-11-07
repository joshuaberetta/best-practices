import __future__
from app.hello_world import printing, sum_nums, split_items
import argparse, os, sys, subprocess, logging, logging.config, yaml

try:
    with open('logging.yaml', 'r') as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
except:
    print('Failed to load config file.')
    logging.basicConfig(level=logging.WARNING)

log = logging.getLogger(__name__)
log.debug('--- NEW DEBUG RUN ---')

parser = argparse.ArgumentParser(description='Hello world! best practices')
parser.add_argument('-t', '--test', action='store_true')
parser.add_argument('-p', '--print', default=None)
parser.add_argument('-sn', '--sum-nums', default=None, nargs='+')
parser.add_argument('-s' ,'--split', default=None, nargs='+')
args = parser.parse_args()

if args.test:
    subprocess.run('python -m unittest discover -v')

if args.print is not None:
    printing(args.print)

if args.sum_nums is not None:
    sum_value = sum_nums(args.sum_nums)
    print(sum_value)

if args.split is not None:
    split = split_items(*args.split)
    print(split)
