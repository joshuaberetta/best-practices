import __future__
import sys, os, logging, inspect
import pandas as pd
from typing import List, Any

log = logging.getLogger(__name__)

def printing(print_val:str) -> None:

    '''Printing out an inputted string to the console

    Args:
        print_val (str): The imput string to be printed out

    Rasises:
        ValueError: Int or float entered instead of string

    Returns:
        None: Printing of imput string to the console
    '''

    try:
        print_val = float(print_val)
    except:
        pass

    log.debug(f'func: {inspect.stack()[0][3]}(), print_val: {print_val}, type: {type(print_val)}')

    if isinstance(print_val, str):
        print(print_val)
    else:
        e = 'str type not used'
        log.exception(e)
        raise ValueError(e)


def sum_nums(list_of_nums:List[Any]) -> float:

    '''Take the sum of a list of numbers

    Args:
        list_of_nums (List[Any]): List of items to be summed, float and/or int
    
    Raises:
        ValueError: Entered non-numeric values in list

    Returns:
        sum (float): Sum of all numeric items in list
    '''

    sum:float = 0.0
    for item in list_of_nums:
        try:
            item = float(item)
        except:
            pass
        
        if not isinstance(item, float):
            e = 'list of ints not supplied'
            log.exception(e)
            raise ValueError(e)
        else:
            sum += item
    
    log.debug(f'func: {inspect.stack()[0][3]}(), list: {list_of_nums} sum: {sum}')

    return sum


def split_items(item:Any, split_on:str=' ') -> List[Any]:
    
    '''Split a string of inputted text on a specified delimeter

    Args:
        item (str): String of words or items to be split
        split_on (str): Delimeter to split the input text on

    Raises:
        LookupError: Delimeter not found in input string of text

    Returns:
        result (List[Any]): List of split items that were seperated by delimeter
    '''

    result:list = []
    idxs:list = []

    if split_on not in str(item) or len(split_on) == 0:
        e = 'Search item not found'
        log.exception(e)
        raise LookupError(e)
    
    for i, val in enumerate(str(item)):
        if val == split_on:
            idxs.append(i)

    start_idx:int = 0
    for i in range(len(idxs)):
        result.append(item[start_idx:idxs[i]])
        start_idx = idxs[i] + 1
    else:
        result.append(item[idxs[-1] + 1:])

    log.debug(f'func: {inspect.stack()[0][3]}(), item: {item}, split: {split_on}, idxs: {idxs}, result: {result}')

    return result
