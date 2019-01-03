from random import randint
class QuickSort:
    def __init__(self,arr):
        self.arr = arr
        self.low = 0
        self.high = len(self.arr)-1
    def Sort(self):
        self.quickSort(self.low,self.high)
        print(self.arr)
        return self.arr
    def quickSort(self,low,high):
        if low >= high:
            return
        mid = self.partion(low,high)
        self.quickSort(low,mid-1)
        self.quickSort(mid+1,high)
    def partion(self,low,high):
        #这里随机生成一个值，也可以直接取low
        pivot = randint(low,high)
        #print(pivot,self.arr[pivot])
        while low < high:
            while low < high and self.arr[high]>self.arr[pivot]:
                high-=1
            while low < high and self.arr[low]<=self.arr[pivot]:
                low+=1
            if low < high:
                self.arr[high],self.arr[low] = self.arr[low],self.arr[high]
        self.arr[low],self.arr[pivot] = self.arr[pivot],self.arr[low]  
        #print(self.arr)     
        return low

        
if __name__ == "__main__":
    QuickSort([1,2,3,4,5,6]).Sort()