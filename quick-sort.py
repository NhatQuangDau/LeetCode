#Quick sort
#inplace sorting - mean no addition memory proportion to the N
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums
    
    def quickSort(self, arr, start, end):
        if start >= end:
            return
        p = self.partition(arr, start, end)
        self.quickSort(arr, start, p - 1)
        self.quickSort(arr, p + 1, end)

    def partition(self, arr, start, end) -> int: #Return the pivot index
        pivot = arr[end]
        pIndex = end # original pivot index
        end -= 1
        while start < end:
            while start < end and arr[start] <= pivot:
                start += 1
            while start < end and arr[end] > pivot:
                end -= 1
            if start<end:
                arr[start], arr[end] = arr[end], arr[start]
        if arr[start] > arr[pIndex]:
            arr[start], arr[pIndex] = arr[pIndex], arr[start]
        else:
            return pIndex 
        return start # new pivot index
