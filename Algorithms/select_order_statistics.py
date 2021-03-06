import random
from quick_sort import partition
import insertion_sort

def select(list,k,start = 0,end = None):
    '''this function takes a list and a integer k as input, and will return the kth largest element'''
    list_length = len(list)
    if start == 0 and end == None:
        list = list.copy()  #copy the original input
    if end == None:
        end = list_length
    index = random.randint(start, end - 1)
    last_num = list[end-1]
    list[end-1] = list[index]
    list[index] = last_num   #exchange a random element to the last position

    _k_ = partition(list,start,end)
    if k == _k_:
        pass
    if k > _k_:
        select(list, k, _k_+1, end)
    if k < _k_:
        select(list, k, start, _k_)
    return list[k]





