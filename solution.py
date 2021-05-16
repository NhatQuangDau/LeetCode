#Simple implementation - generate all permutation possible until permutation kth, then stop, this can solve the problem if input test cases one by one, but when run all test cases, it will be TLE
class Solution:
    dictPer = dict()
    pos = 0
    def getPermutation(self, n: int, k: int) -> str:
        arr = []
        for i in range(1, n+1):
            arr.append(i)
        visited = [False] * n
        self.generatePer(visited, arr, '', k)
        return self.dictPer[k-1]
    def generatePer(self, visited, arr, temp, k):
        if pos == k:
            return
        if len(temp) == len(arr):
            self.dictPer[self.pos] = temp
            self.pos += 1
            return
        for i in range(len(arr)):
            if visited[i] == False:
                visited[i] = True
                temp += str(arr[i])
                self.generatePer(visited, arr, temp, k)
                visited[i] = False
                temp = temp[:-1]
