import random
"""
    三路快速排序处理arr[l...r]
    将arr[l...r]分为 <v; ==v; >v 三部分
    之后递归对<v ; >v 两部分继续进行三路快速排序
"""


def quick_sort(arr,l,r):
    if l > r:
        return False
    start_num = random.randint(l, r)
    arr[start_num], arr[l] = arr[l], arr[start_num]
    v = arr[l]
    lt = l  # arr[l+1...lt] < v
    gt = r + 1  # arr[gt...r] > v
    i = l + 1  # arr[lt+1...i] == v
    while i < gt:
        if arr[i] < v:
            arr[i], arr[lt + 1] = arr[lt + 1], arr[i]
            lt += 1
            i += 1
        elif arr[i] > v:
            arr[i], arr[gt - 1] = arr[gt - 1], arr[i]
            gt -= 1
        else:
            i += 1
    arr[l], arr[lt] = arr[lt], arr[l]
    quick_sort(arr,l,lt-1)
    quick_sort(arr,gt,r)


if __name__ == "__main__":
    nums = [5,3,7,6,1,2]
    quick_sort(nums,0,5)
    print(nums)
