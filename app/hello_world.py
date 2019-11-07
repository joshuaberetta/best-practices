import __future__
import sys, os, logging, ast, inspect
import pandas as pd
from typing import List, Any

log = logging.getLogger(__name__)

def printing(print_val:str) -> None:

    try:
        print_val = int(print_val)
    except:
        pass

    log.debug(f'func: {inspect.stack()[0][3]}(), print_val: {print_val}, type: {type(print_val)}')
    log.warning('testing warning')
    log.debug(f'testing debug')
    
    if isinstance(print_val, str):
        print(print_val)
    else:
        raise ValueError('str type not used')
        


def sum_nums(list_of_nums:List[Any]) -> float:

    sum:float = 0.0
    for item in list_of_nums:
        try:
            item = float(item)
        except:
            pass
        
        if not isinstance(item, float):
            e = 'list of ints not supplied'
            log.exception(e)
            raise Exception(e)
        else:
            sum += item
    
    log.debug(f'func: {inspect.stack()[0][3]}(), sum: {sum}')

    return sum

def split_items(item:Any, split_on:str=' ') -> List[Any]:
    
    result:list = []
    idxs:list = []

    if split_on not in str(item) or len(split_on) == 0:
        raise Exception('Seach item not found')
    
    for i, val in enumerate(str(item)):
        if val == split_on:
            idxs.append(i)

    start_idx:int = 0
    for i in range(len(idxs)):
        result.append(item[start_idx:idxs[i]])
        start_idx = idxs[i] + 1
    else:
        result.append(item[idxs[-1] + 1:])

    return result
