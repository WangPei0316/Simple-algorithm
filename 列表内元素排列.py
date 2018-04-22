"""
一个列表A=[A1，A2，…,An]，要求把列表中所有的组合情况打印出来
"""
from itertools import combinations


def func(iterable):
    for s in range(len(iterable)+1):
        for com in combinations(iterable,s):
            yield com


print(list(func([1,5,8,7,9,3,2])))
