import __future__
import sys, os


def printing(print_val) -> None:
    if isinstance(print_val, str):
        print(print_val, type(print_val))
    else:
        raise Exception('str type not used')
