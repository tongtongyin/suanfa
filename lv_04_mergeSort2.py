def merge(a,b):
    aux = []
    i = 0
    j = 0
    while i<len(a) and j<len(b):
        if a[i] < b[j]:
            aux.append(a[i])
            i += 1
        else:
            aux.append(b[j])
            j += 1
    if i == len(a):
        for x in b[j:]:
            aux.append(x)
    else:
        for y in a[i:]:
            aux.append(y)
    return aux
def Sortmerge(nums):
    if  len(nums)<= 1:
        return nums
    mid = len(nums)//2
    left = nums[:mid]
    right = nums[mid:]
    l = Sortmerge(left)
    r = Sortmerge(right)
    return merge(l,r)
nums = [3,8,1,4,9,6,2,5]
li = Sortmerge(nums)
print(li)



