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
        p = end
        while start <= end:
            if arr[start] > arr[p] and start < p:
                temp = p
                arr[start], arr[temp] = arr[temp], arr[start]
                p = start
            elif arr[start] <= arr[p] and start > p:
                temp = p
                arr[start], arr[temp] = arr[temp], arr[start]
                p = start
            start += 1
        return p
