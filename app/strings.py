from hello_world import split_items, join_items
from typing import List, Any
import logging

log = logging.getLogger(__name__)

class String():

    def __init__(self, item:str):
        self.item = item

    def __repr__(self):
        return f'String: {self.item}'

    def split(self, delimeter:str=' ') -> List[str]:
        items = split_items(self.item, delimeter)
        return items

class L():

    def __init__(self, items:List[Any]):
        self.items = items

    # def __repr__(self):
    #     return f'{self.items}'

    def __repr__(self):
        fmt = ''
        for i, item in enumerate(self.items):
            if i < (len(self.items) - 1):
                fmt += f'{item}, '
            else:
                fmt += f'{item}'
        return f'<<{fmt}>>'

    def __len__(self):
        return len(self.items)

    def __getitem__(self, arg):
        return L(self.items[arg])

    def __setitem__(self, arg, value):
        self.items[arg] = value
        return L(self.items[arg])

    def join(self, delimeter:str=' ') -> str:
        return join_items(self.items, delimeter)

    def _operate_on_items(self, num:float, op=['+', '/', '*']):
        new_items = []
        for item in self.items:
            if isinstance(item, int) or isinstance(item, float):
                if op == '+':
                    new_items.append(float(item) + float(num))
                elif op == '/':
                    new_items.append(float(item) / float(num))
                elif op == '*':
                    new_items.append(float(item) * float(num))
            else:
                raise ValueError('L contains non numeric values')
        return new_items

    def add_num(self, num:float) -> List[float]:
        return L(self._operate_on_items(num=num, op='+'))

    def mult_num(self, num:float) -> List[float]:
        return L(self._operate_on_items(num=num, op='*'))

    def div_num(self, num:float) -> List[float]:
        return L(self._operate_on_items(num=num, op='/'))

    def sum(self) -> float:
        result = 0.0
        for item in self.items:
            if isinstance(item, int) or isinstance(item, float):
                result += float(item)
            else:
                raise ValueError('L contains non numeric values')
        return result

