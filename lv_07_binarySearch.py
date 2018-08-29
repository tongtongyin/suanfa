def binary_search(alist, item):
    """二分查找方法一"""
    first = 0
    last = len(alist) - 1
    while first <= last:
        # 防止出现越界错误
        mid = first+(last-first)//2
        if item == mid:
            return True
        else:
            if item < alist[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return False


def binary_search2(alist, item):
    """二分查找方法2,递归查找"""
    if len(alist) == 0:
        return False
    else:
        mid = len(alist)//2
        if item == alist[mid]:
            return True
        elif item < mid:
            return binary_search(alist[0:mid],item)
        else:
            return binary_search(alist[mid:],item)