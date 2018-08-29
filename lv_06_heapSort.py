class MaxHeap(object):
    def __init__(self, max=100000):
        """初始化堆列表，当前长度，最大长度"""
        self.heapList = [0]
        self.currentSize = 0
        self.maximum = max

    def shift_up(self,i):
        """对索引i的值进行向上调整,满足大顶堆"""
        currentvalue = self.heapList[i]
        while i//2 > 0:
            if currentvalue > self.heapList[i//2]:
                self.heapList[i] = self.heapList[i//2]
                i = i//2
            else:
                break
        self.heapList[i] = currentvalue

    def insert(self,k):
        """将k添加到数组中，并且调整到大顶堆"""
        self.heapList.append(k)
        self.currentSize += 1
        self.shift_up(self.currentSize)
        if self.currentSize > self.maximum:
            self.del_first()
        pass

    def shift_down(self,i):
        """将i索引的元素进行想下调整，满足大顶堆"""
        currentvalue = self.heapList[i]
        while i*2 <= self.currentSize:
            mc = self.max_child(i)
            if currentvalue < mc:
                self.heapList[i] = mc
                i = mc
            else:
                break
        self.heapList[i] = currentvalue

    def max_child(self,i):
        """返回i索引的左右孩子中最大孩子的索引"""
        if i*2+1 > self.currentSize:
            return i*2
        else:
            if self.heapList[i*2+1] > self.heapList[i*2]:
                return i*2+1
            else:
                return i*2

    def del_first(self):
        """取出顶部元素，并且将数组末尾元素放到堆顶，在重新调整为大顶堆"""
        # 保存顶部元素
        retval = self.heapList[1]
        # 如果当前长度为1，那么heaplist = [0,a],
        # 直接将当前长度减一，最后一个元素pop出去，
        # 返回之前保存的第一个元素即可
        if self.currentSize == 1:
            self.currentSize -= 1
            self.heapList.pop()
            return retval
        # 将最后的元素放到顶部，
        self.heapList[1] = self.heapList[self.currentSize]
        # 再pop出去最后的元素
        self.heapList.pop()
        # 那么当前数组长度减一
        self.currentSize -= 1
        # 将放到顶部的元素进行向下调整，保持大顶堆
        self.shift_down(1)
        return retval

    def build_heap(self,alist):
        """将传入的数组原地变成大顶堆"""
        self.heapList = [0] + alist[:]
        self.currentSize = len(alist)
        # 首先i初始化指向堆的第一个非叶子节点
        i = self.currentSize//2
        # 循环往前遍历i，把每个i索引的数向下调整，放到合适位置
        if i > 0:
            self.shift_down(i)
            i -= 1
        # ？？？？？？？？？？？
        overflow = self.currentSize - self.maximum
        for i in range(overflow):
            self.del_first()

    def heap_sort(self, alist):
        """将传入的列表排序"""
        # 首先构造大顶堆
        self.build_heap(alist)
        # 从1到数组长度 依次取出顶部元素放到sortlist列表中，完成从大到小排序
        sortlist = [self.del_first() for x in range(self.currentSize)]
        # 反转数组完成从小到大排序
        sortlist.reverse()
        return sortlist

    def heap_sort2(self,alist):
        """将传入的列表捷星排序第二种方式，原地操作"""
        # 首先构造大顶堆
        self.build_heap(alist)
        # 从当前长度开始循环直到长度为1，
        while self.currentSize > 1:
            # 每次从顶取出元素与当前堆的最后一位互换
            self.heapList[self.currentSize], self.heapList[1] = self.heapList[1], self.heapList[self.currentSize]
            # 长度依次递减
            self.currentSize -= 1
            # 重新调整使满足大顶堆
            self.shift_down(1)
        return self.heapList[1:]
