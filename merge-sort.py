#Merge sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)
    
    def mergeSort(self, arr) -> List[int]:
        mid = len(arr)//2
        if mid == 0:
            return arr
        return self.merge(self.mergeSort(arr[:mid]), self.mergeSort(arr[mid:]))
    
    def merge(self, left, right) -> List[int]:
        i = 0 #index left arr
        j = 0 #index right arr
        l = len(left)
        r = len(right)
        arr = [0]*(l+r)
        k = 0 #index of mergeArr
        while i < l and j < r:
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1
        while i < l:
            arr[k] = left[i]
            i+=1
            k+=1
        while j < r:
            arr[k] = right[j]
            j+=1
            k+=1
        return arr
