import random


def partition(arr,l,r):
    start_num = random.randint(l,r)
    arr[start_num],arr[l] = arr[l],arr[start_num]
    v = arr[l]
    i = l+1
    j = r
    # arr[l+1...i] <= v ; arr(j...r] >= v
    while True:
        while i <= r and arr[i] < v:
            i += 1
        while j >= l+1 and arr[j] > v:
            j -= 1
        if i > j:
            break
        arr[i], arr[j] = arr[j], arr[i];
        i += 1
        j += 1
    arr[j], arr[l] = arr[l], arr[j]
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
