
def insertArr2(nums):
    """
        1. 将当前要排序位置元素保存（复制成副本）
        2. 将副本与前一位置j元素比较，如果副本小于前一元素，将前一元素赋值给 后面位置元素
        3. 在将副本与前一位置j-1元素表，如果副本小于j-1元素，将j-1元素赋值给j元素
    """
    for i in range(1,len(nums)):
        x = nums[i]
        for j in range(i,-1,-1):
            if x < nums[j-1]:
                nums[j] = nums[j-1]
            else:
                break
        nums[j] = x

    return nums

li = [3,2,5,1,4]
insertArr2(li)
print(li)