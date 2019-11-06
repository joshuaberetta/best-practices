import __future__
import sys, os
import pandas as pd
from typing import List, Any


def printing(print_val:str) -> None:

    if isinstance(print_val, str):
        print(print_val)
    else:
        raise Exception('str type not used')


def sum_nums(list_of_nums:List[Any]) -> float:

    sum:float = 0.0
    for item in list_of_nums:
        try:
            item = float(item)
        except:
            pass
        
        if not isinstance(item, float):
            raise Exception('list of ints not supplied')
        else:
            sum += item

    return sum
