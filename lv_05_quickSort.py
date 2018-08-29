import random

def partition(arr,l,r):
    # 设置一个随机下标，使这个下标的数与初始位置互换
    start_num = random.randint(l,r)
    arr[start_num],arr[l] = arr[l],arr[start_num]
    # 设置第一个数为一个标准
    v = arr[l]
    # 设置一个下标j作为最后返回的“中间值”索引,初始设置为第一位的索引
    j = l
    # 循环遍历l-r
    for i in range(l,r+1):
        if arr[i] < v:
            arr[i],arr[j+1] = arr[j+1],arr[i]
            j += 1
    arr[j],arr[l] = arr[l],arr[j]
    return j
def quick_sort(arr,l,r):
    if l > r:
        return False
    p = partition(arr,l,r)
    quick_sort(arr,l,p-1)
    quick_sort(arr,p+1,r)

if __name__ == "__main__":
    nums = [5,3,7,6,1,2]
    quick_sort(nums,0,5)
    print(nums)
