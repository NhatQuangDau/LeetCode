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
        self.quickSort(arr, p, end)

    def partition(self, arr, start, end) -> int: #Return the pivot index
        pivot = arr[(start + end)//2]
        while start <= end:
            while arr[start] < pivot:
                start += 1
            while arr[end] > pivot:
                end -= 1
            if start <= end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        return start
